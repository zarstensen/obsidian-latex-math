import { expect, test } from "vitest";
import { normLatexStr, response_verifier, server } from "../setup";
import { LmatEnvironment } from "/cas/LmatEnvironment";
import { LatexMathSymbol, SolveArgsPayload, SolveInfoArgsPayload, SolveInfoMessage, SolveInfoResponse, SolveMessage, SolveResponse } from "/cas/messages/SolveMessage";

test('Test Solve Message', async () => {
    const response = response_verifier.verifyResponse<SolveResponse>(await server.send(
        new SolveMessage(new SolveArgsPayload("x^2 = 4", new LmatEnvironment(), ["x"], false))
    ).response);

    expect(normLatexStr(response.solution_set)).toMatch(/x\s*=\s*2/g);
    expect(normLatexStr(response.solution_set)).toMatch(/x\s*=\s*-\s*2/g);
});

test('Test Solve Message With Assumptions', async () => {
    const response = response_verifier.verifyResponse<SolveResponse>(await server.send(
        new SolveMessage(new SolveArgsPayload("x^2 = 4", new LmatEnvironment(undefined, undefined, undefined, "Naturals"), ["x"], false))
    ).response);

    expect(normLatexStr(response.solution_set)).toMatch(/x\s*=\s*2/g);
    expect(normLatexStr(response.solution_set)).not.toMatch(/x\s*=\s*-\s*2/g);
});


test('Test Solve Message Multivariate', async () => {
    let response = response_verifier.verifyResponse<SolveResponse>(await server.send(
        new SolveMessage(new SolveArgsPayload("x - y = 0", new LmatEnvironment(), ["x"], false))
    ).response);

    expect(normLatexStr(response.solution_set)).toMatch(/x\s*=\s*y/g);

    response = response_verifier.verifyResponse<SolveResponse>(await server.send(
        new SolveMessage(new SolveArgsPayload("x - y = 0", new LmatEnvironment(), ["y"], false))
    ).response);

    expect(normLatexStr(response.solution_set)).toMatch(/y\s*=\s*x/g);
});

test('Test Solve Info', async () => {
    const response = response_verifier.verifyResponse<SolveInfoResponse>(await server.send(
        new SolveInfoMessage(new SolveInfoArgsPayload("a + b = c", new LmatEnvironment()))
    ).response);

    expect(response.required_symbols).toBe(1);

    expect(response.available_symbols).toEqual([
        { sympy_symbol: 'a', latex_symbol: 'a' } as LatexMathSymbol,
        { sympy_symbol: 'b', latex_symbol: 'b' } as LatexMathSymbol,
        { sympy_symbol: 'c', latex_symbol: 'c' } as LatexMathSymbol
    ]);
});
