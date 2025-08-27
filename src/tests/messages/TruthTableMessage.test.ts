import { expect, test } from "vitest";
import { normLatexStr, response_verifier, server } from "../setup";
import { LmatEnvironment } from "/cas/LmatEnvironment";
import { TruthTableArgsPayload, TruthTableFormat, TruthTableMessage, TruthTableResponse } from "/cas/messages/TruthTableMessage";

test('Test TruthTable Message (markdown)', async () => {
    const response = response_verifier.verifyResponse<TruthTableResponse>(await server.send(
        new TruthTableMessage(new TruthTableArgsPayload("p \\wedge q", new LmatEnvironment(), TruthTableFormat.MARKDOWN))
    ).response);

    const md = response.truth_table;

    expect(md).toContain('|');
    expect(md.split('\n')[0]).toContain("$p$");
    expect(md.split('\n')[0]).toContain("$q$");
});

test('Test TruthTable Message (latex array)', async () => {
    const response = response_verifier.verifyResponse<TruthTableResponse>(await server.send(
        new TruthTableMessage(new TruthTableArgsPayload("p \\vee q", new LmatEnvironment(), TruthTableFormat.LATEX_ARRAY))
    ).response);

    const latex = normLatexStr(response.truth_table);
    expect(latex).toContain("\\begin");
    expect(latex).toContain("\\end");
    expect(latex).toContain("p");
    expect(latex).toContain("q");
});
