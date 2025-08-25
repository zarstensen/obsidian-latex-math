import { ChildProcessWithoutNullStreams } from 'child_process';
import { assert } from 'console';
import getPort from 'get-port';
import { RawData, WebSocket, WebSocketServer } from 'ws';
import { CasClientSpawner } from './LmatCasClientSpawner';

enum MessageType {
    EXIT = "exit",
    START = "start",
    INTERRUPT = "interrupt"
}

enum MessageStatus {
    SUCCESS = "success",
    ERROR = "error",
    INTERRUPTED = "interrupted"
}

export type GenericPayload = Record<string, unknown>;
type ServerPayload = GenericPayload;

// ======== server messages ========

interface ServerMessage {
    readonly type: MessageType;
    readonly payload: ServerPayload;
}

const EXIT_MESSAGE: ServerMessage = {
    type: MessageType.EXIT,
    payload: {}
};

interface ServerMessageUID extends ServerMessage {
    uid: string;
}

export interface StartCommandPayload extends ServerPayload {
    command_type: string;
    start_args: GenericPayload;
}

export class StartCommandMessage implements ServerMessage {
    public readonly type: MessageType = MessageType.START;

    constructor(public readonly payload: StartCommandPayload) { }
}

export interface InterruptHandlerPayload extends ServerPayload {
    target_uids: string[]
}

export class InterruptHandlerMessage implements ServerMessage {
    public type: MessageType = MessageType.INTERRUPT;

    constructor(public payload: InterruptHandlerPayload) { }
}

// ======== client responses ========

export interface ClientResponse {
    status: MessageStatus;
    uid: string;
    payload: GenericPayload;
}

export interface SuccessResponse extends ClientResponse {
    status: MessageStatus.SUCCESS;
    uid: string;
    payload: {
        type: string
        value: GenericPayload
    };
}

export interface ErrorResponse extends ClientResponse {
    status: MessageStatus.ERROR;
    uid: string;
    payload: { 
        usr_message: string;
        dev_message: string;
    };
}

export interface InterrutpedResposne extends ClientResponse {
    status: MessageStatus.INTERRUPTED;
    uid: string;
    payload: Record<string, never>;
}

export type UnixTimestampMillis = number;

interface MessagePromiseEntry {
    sent_time: UnixTimestampMillis;
    resolve: (value: ClientResponse | PromiseLike<ClientResponse>) => void;
    reject: (reason?: unknown) => void;
}

// The LmatCasServer class manages a connection as well as message encoding and handling, with an LmatCasClient script instance.
// Also manages the python process itself.
export class CasServer {
    // Start the LmatCasClient python process, and establish an connection to it.
    // cas_client_spawner: a CasClientSpawner instance, used to spawn a cas client and connect it to the constructed server.
    public async initializeAsync(cas_client_spawner: CasClientSpawner): Promise<void> {
        // Start by setting up the web socket server, so we can get a port to give to the python program.
        const server_port = await getPort();
        
        this.ws_cas_server = new WebSocketServer({ 
            port: server_port
        });
        
        // now start the client process
        this.client_process = await cas_client_spawner.spawnClient(server_port);
        
        // setup output to be logged in the developer console
        this.client_process.stdout.on('data', (data) => {
            console.log('lmat-cas-client stdout:\n' + data.toString());
        });
        
        this.client_process.stderr.on('data', (data) => {
            console.error('lmat-cas-client stderr:\n' + data.toString());
        });
        
        this.client_process.on('close', (code) => {
            console.log(`child process exited with code ${code}`);
            // TODO: do something here
        });

        // wait for the process to establish a connection
        this.ws_cas_client = await new Promise(this.resolveConnection.bind(this));
        this.ws_cas_client.on('message', (buffer) => this.handleMessage(buffer));
        this.is_running = true;
    }

    // Close server / client connection, and shutdown client process.
    // If [timeout] seconds passes without the client shutting down gracefully, it is forcefully killed.
    public async shutdown(timeout: number): Promise<void> {
        this.is_running = false;

        let shutdown_timeout: NodeJS.Timeout | undefined;

        const timeout_promise = new Promise<void>((_, reject) => {
            shutdown_timeout = setTimeout(() => reject(new Error("Timeout")), timeout * 1000);
        });

        const shutdown_promise = (async () => {
            const result = await this.send(EXIT_MESSAGE);
            assert(result.status === MessageStatus.SUCCESS);
        })();

        let shutdown_error: Error | undefined = undefined;

        try {
            await Promise.race([shutdown_promise, timeout_promise]);
        } catch (error) {
            shutdown_error = Error("Shutdown failed or timedout", { cause: error });
            this.client_process.kill();
        }

        clearTimeout(shutdown_timeout);
        this.ws_cas_client.close();
        this.ws_cas_server.close();

        if(shutdown_error !== undefined) {
            throw shutdown_error;
        }
    }

    // Assign an error callback handler.
    // This callback is called any time an error message is received from the cas client process.
    // It is passed the following two strings:
    //      usr_error: A user friendly(ish) string describing the error.
    //      dev_error: A full stack trace of the python exception.
    public onError(callback: (usr_error: string, dev_error: string) => void): void {
        this.error_callback = callback;
    }

    // Send a message to the cas client.
    public async send(message: ServerMessage): Promise<SuccessResponse> {
         const server_message: ServerMessageUID = {
            type: message.type,
            uid: crypto.randomUUID(),
            payload: message.payload
        };

        const result_promise =  new Promise<SuccessResponse>((resolve, reject) => {
            this.message_promises[server_message.uid] = {
                sent_time: this.getTime(),
                resolve: resolve,
                reject: reject,
            };
        });

        this.ws_cas_client.send(JSON.stringify(server_message));
        
        return await result_promise;
    }

    // retreive a list of UID's of messages who has not responded for more than min_hang_time ms.
    public getHangingMessages(options: { min_hang_time: UnixTimestampMillis }): string[] {
        const current_time = this.getTime();

        return Object.keys(this.message_promises).filter((key) => {
            const entry = this.message_promises[key];
            return current_time - entry.sent_time >= options.min_hang_time;
        });
    }

    // retreive a list of all message UID's who are currently missing a response.
    public getCurrentMessages(): string[] {
        return this.getHangingMessages({ min_hang_time: 0 });
    }

    
    private client_process: ChildProcessWithoutNullStreams;
    private ws_cas_client: WebSocket;
    private ws_cas_server: WebSocketServer;
    private error_callback: (usr_error: string, dev_error: string) => void;

    private message_promises: Record<string, MessagePromiseEntry> = { };


    private resolveConnection(resolve: (value: WebSocket) => void, _reject: (reason: string) => void) {
        this.ws_cas_server.once('connection', (ws) => {
            resolve(ws);
        });
    }

    // Handle a response from the cas client.
    // The contents of the client response is resolved through the promise returned from a corresponding send call.
    // i.e.
    // await send() -> message has uid 1 -> response with uid 1 is resolved.
    // await handleMessage() -> makes sure that the send promise is resolved.
    private handleMessage(response_buffer: RawData): void {
        const response: ClientResponse = JSON.parse(response_buffer.toString());

        // first retreive the message promise to resolve (if present).

        let message_promise: MessagePromiseEntry | null = null;

        if (this.message_promises[response.uid] !== undefined) {
            message_promise = this.message_promises[response.uid];
            delete this.message_promises[response.uid];
        }

        // now handle the response depending on its status.
        
        switch (response.status) {
            case MessageStatus.ERROR: {
                const err = response as ErrorResponse;

                if(this.error_callback) {
                    this.error_callback(err.payload.usr_message, err.payload.dev_message);
                }
                
                message_promise?.reject(err.payload.dev_message);
                break;
            }
            case MessageStatus.INTERRUPTED: {
                message_promise?.reject("Interrupted");
                break;
            }
            case MessageStatus.SUCCESS: {
                message_promise?.resolve(response);
                break;
            }
            default: {
                const err_msg = `Unknown response status: ${response.status}`;
                this.error_callback(err_msg, err_msg);
            }
        }
    }

    private getTime(): UnixTimestampMillis {
        return Date.now();
    }
}
