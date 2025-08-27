import { expect, test } from "vitest";
import { normLatexStr, response_verifier, server } from "../setup";
import { LmatEnvironment } from "/cas/LmatEnvironment";
import { SymbolSetArgsPayload, SymbolSetMessage, SymbolSetResponse } from "/cas/messages/SymbolSetsMessage";

test('Test SymbolSets Message (with assumptions)', async () => {
    const env = new LmatEnvironment({
        x: [ "real" ],
        n: [ "integer" ],
    });

    const response = response_verifier.verifyResponse<SymbolSetResponse>(await server.send(
        new SymbolSetMessage(new SymbolSetArgsPayload(env))
    ).response);

    const latex = normLatexStr(response.symbol_sets);
    
    // Should include x and n followed by the relevant set symbol

    expect(latex).toMatch(/x(?:(?!\\\\).)*R/);
    expect(latex).toMatch(/n(?:(?!\\\\).)*Z/);
});
