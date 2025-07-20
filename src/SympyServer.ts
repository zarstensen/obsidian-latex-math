import { WebSocket, WebSocketServer } from 'ws';
import getPort from 'get-port';
import { ChildProcessWithoutNullStreams } from 'child_process';
import { SympyClientSpawner } from './SympyClientSpawner';
import { assert } from 'console';
import { LmatEnvironment } from './LmatEnvironment';

enum MessageType {
    EXIT = "exit",
    START = "start",
    COMM = "comm",
    INTERRUPT = "interrupt"
}

type ServerPayload = Record<string, unknown>;

interface ServerMessage {
    readonly type: MessageType;
    readonly payload: ServerPayload;
}

interface ServerMessageUID extends ServerMessage {
    uid: string;
}

const EXIT_MESSAGE: ServerMessage = {
    type: MessageType.EXIT,
    payload: {}
};

interface StartPayload extends ServerPayload {
    command: string;
    expression: string;
    environment: LmatEnvironment
}

export class StartMessage implements ServerMessage {
    public readonly type: MessageType = MessageType.START;

    constructor(public readonly payload: StartPayload) { }
}

interface InterruptPayload extends ServerPayload {
    target_uid: string
}

export class InterruptMessage implements ServerMessage {
    public type: MessageType = MessageType.INTERRUPT;

    constructor(public payload: InterruptPayload) { }
}

interface ClientResponse {
    status: string;
    uid: string;
    result: Record<string, unknown>;
}

interface ClientError {
    status: "error";
    uid: string;
    result: { 
        usr_message: string;
        dev_message: string;
    };
}

interface MessagePromiseEntry {
    resolve: (value: ClientResponse | PromiseLike<ClientResponse>) => void;
    reject: (reason?: unknown) => void;
}

// so in here all of the different communications are ASYNC, where as in the sympy process, each communication is on a new thread i guess?

// The SympyServer class manages a connection as well as message encoding and handling, with an SympyClient script instance.
// Also manages the python process itself.
export class SympyServer {
    // Start the SympyClient python process, and establish an connection to it.
    // vault_dir: the directory of the vault, which thsi plugin is installed in.
    // python_exec: the python executable to use to start the SympyClient process.
    public async initializeAsync(sympy_client_spawner: SympyClientSpawner): Promise<void> {
        // Start by setting up the web socket server, so we can get a port to give to the python program.
        const server_port = await getPort();

        this.ws_python_server = new WebSocketServer({ 
            port: server_port
        });

        // now start the python process
        this.python_process = await sympy_client_spawner.spawnClient(server_port);
        
        
        // setup output to be logged in the developer console
        let stdout_buffer = "";
        let stderr_buffer = "";

        this.python_process.stdout.on('data', (data) => {
            console.log(data.toString());
            stdout_buffer += data.toString();
        });

        this.python_process.stdout.on('end', () => {
            if(stdout_buffer) {
                console.log(`stdout: \n${stdout_buffer}`);
                stdout_buffer = '';
            }
        });


        this.python_process.stderr.on('data', (data) => {
            console.error(data.toString());
            stderr_buffer += data.toString();
        });

        this.python_process.stderr.on('end', () => {
            if(stderr_buffer) {
                console.error(`stderr: \n${stderr_buffer}`);
                stderr_buffer = '';
            }
        });

        this.python_process.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
            // TODO: do something here
        });

        // wait for the process to establish an connection
        this.ws_python = await new Promise(this.resolveConnection.bind(this));
    }

    // Close server / client connection, and shutdown client process.
    // If [timeout] seconds passes without the client shutting down gracefully, it is forcefully killed.
    public async shutdown(timeout: number): Promise<void> {
        let shutdown_timeout: NodeJS.Timeout | undefined;

        const timeout_promise = new Promise<void>((_, reject) => {
            shutdown_timeout = setTimeout(() => reject(new Error("Timeout")), timeout * 1000);
        });

        const shutdown_promise = (async () => {
            const result = await this.send(EXIT_MESSAGE);
            assert(result.status === "exit");
        })();

        let shutdown_error: Error | undefined = undefined;

        try {
            await Promise.race([shutdown_promise, timeout_promise]);
        } catch (error) {
            shutdown_error = Error("Shutdown failed or timedout", { cause: error });
            this.python_process.kill();
        }

        clearTimeout(shutdown_timeout);
        this.ws_python.close();
        this.ws_python_server.close();

        if(shutdown_error !== undefined) {
            throw shutdown_error;
        }
    }

    // Assign an error callback handler.
    // This callback is called any time an error message is received from the SympyClient process.
    // It is passed the following two strings:
    //      usr_error: A user friendly(ish) string describing the error.
    //      dev_error: A full stack trace of the python exception.
    public onError(callback: (usr_error: string, dev_error: string) => void): void {
        this.error_callback = callback;
    }

    // Send a message to the SympyClient process.
    public async send(message: ServerMessage): Promise<ClientResponse> {
        return await this.reply(message, crypto.randomUUID());
    }

    public async reply(message: ServerMessage, communication_uid: string) {
        const server_message: ServerMessageUID = {
            type: message.type,
            uid: communication_uid,
            payload: message.payload
        };

        const result_promise =  new Promise<ClientResponse>((resolve, reject) => {
            this.message_promises[server_message.uid] = {
                resolve: resolve,
                reject: reject,
            };
        });

        this.ws_python.send(JSON.stringify(server_message));
        
        return await result_promise;
    }

    // Receive a result from the SympyClient process.
    // Returns a promise that resolves to the result object, parsed from the received json payload.
    public async receive(): Promise<void> {
        return new Promise((resolve, _reject) => {
            this.ws_python.once('message', (result_buffer) => {
                const result: ClientResponse = JSON.parse(result_buffer.toString());
                
                // first retreive the message promise to resolve (if present).

                let message_promise: MessagePromiseEntry | null = null;
                
                if (this.message_promises[result.uid] !== undefined) {
                    message_promise = this.message_promises[result.uid];
                    delete this.message_promises[result.uid];
                }
                
                // first some special cases.

                if (result.status === "error") {
                    
                    const err = result as ClientError;

                    if(this.error_callback) {
                        this.error_callback(err.result.usr_message, err.result.dev_message);
                    }
                    
                    message_promise?.reject(err.result.dev_message);
                    resolve();
                } else {
                    message_promise?.resolve(result);
                    resolve();
                }
            });
        });
    }

    private python_process: ChildProcessWithoutNullStreams;
    private ws_python: WebSocket;
    private ws_python_server: WebSocketServer;
    private error_callback: (usr_error: string, dev_error: string) => void;

    private message_promises: Record<string, MessagePromiseEntry> = { };

    private resolveConnection(resolve: (value: WebSocket) => void, reject: (reason: string) => void) {
        this.ws_python_server.once('connection', (ws) => {
            resolve(ws);
        });
    }
}
