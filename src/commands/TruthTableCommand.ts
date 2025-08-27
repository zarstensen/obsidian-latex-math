import { App, Editor, MarkdownView, Notice } from "obsidian";
import { CasServer } from "cas/LmatCasServer";
import { LatexMathCommand } from "./LatexMathCommand";
import { EquationExtractor } from "EquationExtractor";
import { LmatEnvironment } from "cas/LmatEnvironment";
import { formatLatex } from "FormatLatex";
import { TruthTableArgsPayload, TruthTableFormat, TruthTableMessage, TruthTableResponse } from "cas/messages/TruthTableMessage";

export class TruthTableCommand extends LatexMathCommand {
    readonly id: string;

    constructor(public format: TruthTableFormat, ...base_args: ConstructorParameters<typeof LatexMathCommand>) {
        super(...base_args);
        this.truth_table_format = format;
        this.id = `generate-${this.truth_table_format}-truth-table`;
    }

    async functionCallback(cas_server: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        // Extract the proposition to generate truth table for
        const equation = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);

        if (equation === null) {
            new Notice("You are not inside a math block");
            return;
        }

        const lmat_env = LmatEnvironment.fromMarkdownView(app, view);

        // Send it to python.
        const response = await cas_server.send(new TruthTableMessage(
            new TruthTableArgsPayload(equation.contents, lmat_env, this.truth_table_format)
        )).response;

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
