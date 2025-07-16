import { WebSocket, WebSocketServer } from 'ws';
import getPort from 'get-port';
import { ChildProcessWithoutNullStreams } from 'child_process';
import { SympyClientSpawner } from './SympyClientSpawner';
import { assert } from 'console';

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
        this.python_process.stdout.on('data', (data) => {
            console.log(`stdout: ${data}`);
        });

        this.python_process.stderr.on('data', (data) => {
            console.error(`stderr: ${data}`);
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
            await this.send("exit", {});
            const result = await this.receive();
            assert(result === "exit");
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
    public async send(mode: string, data: unknown): Promise<void> {
        await this.initialized_promise;
        this.ws_python.send(mode + "|" + JSON.stringify(data));
    }

    // Receive a result from the SympyClient process.
    // Returns a promise that resolves to the result object, parsed from the received json payload.
    public async receive(): Promise<any> {
        return new Promise((resolve, reject) => {
            this.ws_python.once('message', (result_buffer) => {
                const result = result_buffer.toString();
                const separator_index = result.indexOf("|");
                
                const status = result.substring(0, separator_index);
                const payload = JSON.parse(result.substring(separator_index + 1));

                if (status === "error") {
                    
                    if(this.error_callback) {
                        this.error_callback(payload.usr_message, payload.dev_message);
                    }

                    reject(payload.dev_message);
                } else if(status === "exit") {
                    resolve("exit");
                } else {
                    resolve(payload);
                }
            });
        });
    }

    private initialized_promise: Promise<void>;
    private python_process: ChildProcessWithoutNullStreams;
    private ws_python: WebSocket;
    private ws_python_server: WebSocketServer;
    private error_callback: (usr_error: string, dev_error: string) => void;

    private resolveConnection(resolve: (value: WebSocket) => void, reject: (reason: string) => void) {
        this.ws_python_server.once('connection', (ws) => {
            resolve(ws);
        });
    }
}
