import { expect, test } from "vitest";
import { normLatexStr, response_verifier, server } from "../setup";
import { EvaluateArgsPayload, EvaluateMessage, EvaluateMode, EvaluateResponse, UnitConvertArgsPayload } from "/cas/messages/EvaluateMessage";
import { LmatEnvironment } from "/cas/LmatEnvironment";

test('Test Eval Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.EVAL, new EvaluateArgsPayload("1 + 1", new LmatEnvironment()))
    ).response);

    expect(response.evaluated_expression).toBe("2");
});

test('Test Evalf Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.EVALF, new EvaluateArgsPayload("\\frac{1}{2}", new LmatEnvironment()))
    ).response);

    expect(normLatexStr(response.evaluated_expression)).toBe(normLatexStr("0.5"));
});

test('Test Expand Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.EXPAND, new EvaluateArgsPayload("(a + b) \\cdot 2", new LmatEnvironment()))
    ).response);

    expect(normLatexStr(response.evaluated_expression)).toBe(normLatexStr("2 a + 2 b"));
});


test('Test Factor Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.FACTOR, new EvaluateArgsPayload("x^2 - 1", new LmatEnvironment()))
    ).response);

    expect(normLatexStr(response.evaluated_expression)).toBe(normLatexStr("(x - 1) (x + 1)"));
});


test('Test Apart Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.APART, new EvaluateArgsPayload("\\frac{1}{x^2 - x}", new LmatEnvironment()))
    ).response);

    expect(normLatexStr(response.evaluated_expression)).toBe(normLatexStr("\\frac{1}{x - 1} - \\frac{1}{x}"));
});

test('Test Unit Convert Message', async () => {
    const response = response_verifier.verifyResponse<EvaluateResponse>(await server.send(
        new EvaluateMessage(EvaluateMode.CONVERT_UNITS, new UnitConvertArgsPayload("120 {s}", new LmatEnvironment(), [ "min" ]))
    ).response);

    expect(normLatexStr(response.evaluated_expression)).toBe(normLatexStr("2 {min}"));
});
