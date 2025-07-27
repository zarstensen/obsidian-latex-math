import { App, Editor, MarkdownView, Notice } from "obsidian";
import { GenericPayload, StartCommandMessage, SympyServer } from "src/SympyServer";
import { LatexMathCommand } from "./LatexMathCommand";
import { EquationExtractor } from "src/EquationExtractor";
import { LmatEnvironment } from "src/LmatEnvironment";
import { LatexMathSymbol, SolveModeModal } from "src/SolveModeModal";
import { formatLatex } from "src/FormatLatex";

class SolveArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
        public symbols: string[]
    ) { }
    [x: string]: unknown;
}

interface SolveResult {
    solution_set: string
}


class SolveInfoPayload implements GenericPayload {
        public constructor(
        public expression: string,
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}


interface SolveInfoResult {
    required_symbols: number
    available_symbols: LatexMathSymbol[],
}

export class SolveCommand extends LatexMathCommand {
    readonly id: string = 'solve-latex-expression';

    async functionCallback(evaluator: SympyServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        // Extract the equation to solve
        const equation = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);

        if (equation === null) {
            new Notice("You are not inside a math block");
            return;
        }

        const lmat_env = LmatEnvironment.fromMarkdownView(app, view);

        // Send it to python to get some information about it.

        const solve_info_response = await evaluator.send(new StartCommandMessage({
            command_type: "solve-info",
            start_args: new SolveInfoPayload(equation.contents, lmat_env)
        }));

        const solve_info_result = this.verifyResponse<SolveInfoResult>(solve_info_response);

        console.log(solve_info_result);

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

        const solve_response = await evaluator.send(new StartCommandMessage({
            command_type: "solve",
            start_args: new SolveArgsPayload(equation.contents, lmat_env, [...symbols].map((symbol) => symbol.sympy_symbol)),
        }));

        const solve_result = this.verifyResponse<SolveResult>(solve_response);

        // Insert solution as a new math block, right after the current one.
        editor.replaceRange("\n$$" + await formatLatex(solve_result.solution_set) + "$$", editor.offsetToPos(equation.block_to));
        editor.setCursor(editor.offsetToPos(equation.to + solve_result.solution_set.length + 3));

    }
    
}
