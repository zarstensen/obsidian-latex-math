import { SuccessResponse } from "./LmatCasServer";

export class SuccessResponseVerifier {
    public verifyResponse<T>(response: SuccessResponse, expected_types: Set<string> = new Set(['result'])): T {
        if(!expected_types.has(response.payload.type)) {
            this.triggerVerifyFailure(response, expected_types);
            throw new Error(`Invalid response type: ${response.payload.type}\nExpected one of the following: ${[...expected_types]}`);
        }

        return response.payload.value as T;
    }

    private on_verify_failure_callbacks: Array<(command: unknown, response: SuccessResponse, expected_statuses: Set<string>) => void> = [];

    public onVerifyFailure(callback: (command: unknown, response: SuccessResponse, expected_statuses: Set<string>) => void): void {
        this.on_verify_failure_callbacks.push(callback);
    }

    protected triggerVerifyFailure(response: SuccessResponse, expected_statuses: Set<string>): void {
        for (const callback of this.on_verify_failure_callbacks) {
            callback(this, response, expected_statuses);
        }
    }
}
