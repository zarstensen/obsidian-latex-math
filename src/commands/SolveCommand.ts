import { App, Editor, MarkdownView, Notice } from "obsidian";
import { EquationExtractor } from "src/EquationExtractor";
import { formatLatex } from "src/FormatLatex";
import { CasServer, GenericPayload, StartCommandMessage } from "src/LmatCasServer";
import { LmatEnvironment } from "src/LmatEnvironment";
import { LatexMathSymbol, SolveModeModal } from "src/modals/SolveModeModal";
import { LatexMathCommand } from "./LatexMathCommand";

class SolveArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
        public symbols: string[]
    ) { }
    [x: string]: unknown;
}

interface SolveResponse {
    solution_set: string
}

class SolveInfoArgsPayload implements GenericPayload {
        public constructor(
        public expression: string,
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}


interface SolveInfoResponse {
    required_symbols: number
    available_symbols: LatexMathSymbol[],
}

export class SolveCommand extends LatexMathCommand {
    readonly id: string = 'solve-latex-expression';

    public constructor(...base_args: ConstructorParameters<typeof LatexMathCommand>) {
        super(...base_args);
    }

    async functionCallback(cas_server: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        // Extract the equation to solve
        const equation = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);

        if (equation === null) {
            new Notice("You are not inside a math block");
            return;
        }

        const lmat_env = LmatEnvironment.fromMarkdownView(app, view);

        // Send expression to cas server to get some information about it.

        const solve_info_response = await cas_server.send(new StartCommandMessage({
            command_type: "solve-info",
            start_args: new SolveInfoArgsPayload(equation.contents, lmat_env)
        }));

        const solve_info_result = this.response_verifier.verifyResponse<SolveInfoResponse>(solve_info_response);

        let symbols: LatexMathSymbol[] = [ ];

        if(solve_info_result.available_symbols.length > solve_info_result.required_symbols) {
            const symbol_selector = new SolveModeModal(
                solve_info_result.available_symbols,
                solve_info_result.required_symbols,
                lmat_env.domain ?? "",
                app);

            symbol_selector.open();

            const config = await symbol_selector.getSolveConfig();
            lmat_env.domain = config.domain;

            symbols = config.symbols;
        } else {
            symbols = solve_info_result.available_symbols.slice(0, solve_info_result.required_symbols);
        }

        // actually solve the equation now, with the symbols configured automatically or by the user.

        const solve_response = await cas_server.send(new StartCommandMessage({
            command_type: "solve",
            start_args: new SolveArgsPayload(equation.contents, lmat_env, [...symbols].map((symbol) => symbol.sympy_symbol)),
        }));

        const solve_result = this.response_verifier.verifyResponse<SolveResponse>(solve_response);

        // insert solution as a new math block, right after the current one.
        editor.replaceRange("\n$$" + await formatLatex(solve_result.solution_set) + "$$", editor.offsetToPos(equation.block_to));
        editor.setCursor(editor.offsetToPos(equation.to + solve_result.solution_set.length + 3));

    }
    
}
