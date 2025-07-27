import { App, Editor, MarkdownView } from "obsidian";
import { ClientResponse, GenericPayload, SuccessResponse, SympyServer } from "src/SympyServer";

// Interface for a latex math command
// The id will be used to set the resulting obsidian command id.
// function callback is called whenever the command has been invoked by the user.
export abstract class LatexMathCommand {
    readonly id: string;

    abstract functionCallback(evaluator: SympyServer, app: App, editor: Editor, view: MarkdownView): Promise<void>; // Method to execute the command

    public verifyResponse<T>(response: SuccessResponse, expected_types: Set<string> = new Set([ 'result' ])): T {

        const response_is_expected = expected_types.has(response.payload.type);

        if(!response_is_expected) {
            this.triggerVerifyFailure(response, expected_types);
            throw new Error(`Unexpected response type: ${response.payload.type}\nExpected one of the following: ${[...expected_types]}`);
        }

        return response.payload.value as T;
    }

    private on_verify_failure_callbacks: Array<(command: LatexMathCommand, response: ClientResponse, expected_statuses: Set<string>) => void> = [];

    public onVerifyFailure(callback: (command: LatexMathCommand, response: ClientResponse, expected_statuses: Set<string>) => void): void {
        this.on_verify_failure_callbacks.push(callback);
    }

    protected triggerVerifyFailure(response: ClientResponse, expected_statuses: Set<string>): void {
        for (const callback of this.on_verify_failure_callbacks) {
            callback(this, response, expected_statuses);
        }
    }

}