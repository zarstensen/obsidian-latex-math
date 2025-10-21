import { afterEach, assert, beforeEach } from "vitest";
import { SourceCodeSpawner } from "../models/cas/LmatCasClientSpawner";
import { CasServer } from "../models/cas/LmatCasServer";
import { SuccessResponseVerifier } from "../models/cas/ResponseVerifier";

export let server: CasServer;
export const response_verifier: SuccessResponseVerifier = new SuccessResponseVerifier();
let server_err: string | undefined;

response_verifier.onVerifyFailure((command, response, expected_statuses) => {
    assert.fail(`Expected one of ${expected_statuses.toString()} got ${response.status}`);
});

export function normLatexStr(latex_str: string): string {
    return latex_str.replace(/(\\,|\s)+/g, ' ').replace(/(\\left|\\right)/g, '');
}

beforeEach(async () => {
    server = new CasServer();
    server_err = undefined;

    server.onError((_usr_error: string, dev_error: string) => {
        server_err = dev_error;
    });

    await server.initializeAsync(new SourceCodeSpawner('./'));

}, 60000);

afterEach(async () => {
    if (server !== undefined) {
        await server.shutdown(10);
    }

    if (server_err !== undefined) {
        assert.fail(server_err);
    }
}, 60000);
