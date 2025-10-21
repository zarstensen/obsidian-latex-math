import { expect, test } from "vitest";
import { Definition, LmatEnvironment } from "../models/cas/LmatEnvironment";

test('Test LmatEnvironment.parseDefinitions', async () => {
    const definitions = LmatEnvironment.parseDefinitions(`
        $x := 25$
        $f(x) := x^2$
        $ y := $
        $x_y := x + y$
        $\\pmb{x} := x + y$
        $ 1 + 2 + 3 = 6$
        $ := 25$
        `);

    expect(definitions).toEqual([
        { name_expr: "x", value_expr: "25" } as Definition,
        { name_expr: "f(x)", value_expr: "x^2" } as Definition,
        { name_expr: "y", value_expr: "" } as Definition,
        { name_expr: "x_y", value_expr: "x + y" } as Definition,
        { name_expr: "\\pmb{x}", value_expr: "x + y" } as Definition,
    ]);
});
