import { expect, test } from "vitest";
import { LmatEnvironment } from "../models/cas/LmatEnvironment";

test('Test LmatEnvironment.parseDefinitions', async () => {
    const definitions = LmatEnvironment.parseDefinitions(`
        $x := 25$
        $f(x) := x^2$
        $ y := $
        $x_y := x + y$
        $\\pmb{x} := x + y$
        $ 1 + 2 + 3 = 6$
        Some text here
        $ := 25$

        \\$ not a definition := definition a not $ \\$ $
        `);

    expect(definitions).toEqual([
        "x := 25",
        "f(x) := x^2",
        " y := ",
        "x_y := x + y",
        "\\pmb{x} := x + y",
        " := 25",
    ]);
});
