import { SuccessResponse } from "./LmatCasServer";

// SuccessResponseVerifier is responsible for verifying a SuccessResponse instance, as well as providing an interface for 
// providing error handlers for verify failures.
export class SuccessResponseVerifier {
    // Verify the given response has one of the given response types.
    // default expected type is 'result'.
    // if verification is failed, an error is thrown, and the VerifyFailure event is triggered.
    public verifyResponse<T>(response: SuccessResponse, expected_types: Set<string> = new Set(['result'])): T {
        if(!expected_types.has(response.payload.type)) {
            this.triggerVerifyFailure(response, expected_types);
            throw new Error(`Invalid response type: ${response.payload.type}\nExpected one of the following: ${[...expected_types]}`);
        }

        return response.payload.value as T;
    }

    private on_verify_failure_callbacks: Array<(command: unknown, response: SuccessResponse, expected_statuses: Set<string>) => void> = [];

    // register a VerifyFailure event handler.
    // these handlers are triggered any time verifyResponse fails.
    public onVerifyFailure(callback: (command: unknown, response: SuccessResponse, expected_statuses: Set<string>) => void): void {
        this.on_verify_failure_callbacks.push(callback);
    }

    protected triggerVerifyFailure(response: SuccessResponse, expected_statuses: Set<string>): void {
        for (const callback of this.on_verify_failure_callbacks) {
            callback(this, response, expected_statuses);
        }
    }
}
