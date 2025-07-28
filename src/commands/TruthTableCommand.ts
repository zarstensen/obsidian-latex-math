import { App, Editor, MarkdownView, Notice } from "obsidian";
import { GenericPayload, StartCommandMessage, SympyServer } from "src/SympyServer";
import { LatexMathCommand } from "./LatexMathCommand";
import { EquationExtractor } from "src/EquationExtractor";
import { LmatEnvironment } from "src/LmatEnvironment";
import { formatLatex } from "src/FormatLatex";

class TruthTablePayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
        public truth_table_format: TruthTableFormat
    ) { }
    [x: string]: unknown;
}

interface TruthTableResponse {
    truth_table: string
}

// Enum of all possible truth table formats returned by the sympy client
export enum TruthTableFormat {
    // truth table contents is formatted as a markdown table with latex entries.
    MARKDOWN = "md",
    // truth table is formatted in a latex array, displayable by mathjax 
    LATEX_ARRAY = "latex-array",
    // TODO: LATEX_TABLE?
    // this is not supported by mathjax, but could be usefull for real latex documents?
}

export class TruthTableCommand extends LatexMathCommand {
    readonly id: string;

    constructor(public format: TruthTableFormat, ...base_args: ConstructorParameters<typeof LatexMathCommand>) {
        super(...base_args);
        this.truth_table_format = format;
        this.id = `generate-${this.truth_table_format}-truth-table`;
    }

    async functionCallback(evaluator: SympyServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        // Extract the proposition to generate truth table for
        const equation = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);

        if (equation === null) {
            new Notice("You are not inside a math block");
            return;
        }

        const lmat_env = LmatEnvironment.fromMarkdownView(app, view);

        // Send it to python.
        const response = await evaluator.send(new StartCommandMessage({
            command_type: "truth-table",
            start_args: new TruthTablePayload(equation.contents, lmat_env, this.truth_table_format)
        }));

        const result = this.response_verifier.verifyResponse<TruthTableResponse>(response);

        // Insert truth table right after the current math block.
        let insert_content: string = "\n\n" + result.truth_table;

        if(this.format == TruthTableFormat.LATEX_ARRAY) {
            insert_content = "\n$$\n" + await formatLatex(insert_content) + "\n$$";
        }

        editor.replaceRange(insert_content, editor.offsetToPos(equation.block_to));
        editor.setCursor(editor.offsetToPos(equation.to + insert_content.length));
    }
 
    private readonly truth_table_format: TruthTableFormat;
}
