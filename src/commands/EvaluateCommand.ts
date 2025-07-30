import { App, Editor, EditorPosition, MarkdownView, Notice } from "obsidian";
import { CasServer, StartCommandMessage, GenericPayload } from "src/LmatCasServer";
import { LatexMathCommand } from "./LatexMathCommand";
import { EquationExtractor } from "src/EquationExtractor";
import { LmatEnvironment } from "src/LmatEnvironment";
import { formatLatex } from "src/FormatLatex";

interface EvaluateResponse {
    metadata: {
        separator: string,
        end_line: number
    },
    evaluated_expression: string
}

export class EvalArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}

export type Expression = { from: number, to: number, contents: string, is_multiline: boolean };

export class EvaluateCommand extends LatexMathCommand {
    readonly id: string;

    constructor(evaluate_mode: string, ...base_args: ConstructorParameters<typeof LatexMathCommand>) {
        super(...base_args);
        this.id = `${evaluate_mode}-latex-expression`;
        this.evaluate_mode = evaluate_mode;
    }
    
    public async functionCallback(evaluator: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
                
        const expression = this.get_expression(editor);

        if (expression === null) {
            new Notice("You are not inside a math block");
            return;
        }

        // send it to python and wait for response.
        const response = await evaluator.send(new StartCommandMessage({
            command_type: this.evaluate_mode,
            start_args: await this.create_args_payload(expression, app, view)
        }));

        const result = this.response_verifier.verifyResponse<EvaluateResponse>(response);

        await this.insert_response(result, expression, editor);
    }

    protected get_expression(editor: Editor): Expression | null {
        let expression: Expression | null
                        = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);

        if(editor.getSelection().length > 0) {
            expression = {
                from: editor.posToOffset(editor.getCursor('from')),
                to: editor.posToOffset(editor.getCursor('to')),
                contents: editor.getSelection(),
                is_multiline: expression?.is_multiline ?? false
            };
        }

        return expression;
    }

    protected async insert_response(response: EvaluateResponse, expression: Expression, editor: Editor): Promise<void> {

        const insert_pos: EditorPosition = editor.offsetToPos(expression.to);
        let insert_content = ` ${response.metadata.separator} ` + await formatLatex(response.evaluated_expression);

        // remove any newlines from the formatted latex if the math block does not support newlines.
        if(!expression.is_multiline) {
            insert_content = insert_content.replaceAll('\n', ' ');
        }

        // check if we have gotten a preferred insert position from the cas client,
        // if not just place it at the end of the expression.
        if (response.metadata.end_line !== undefined) {
            insert_pos.line = editor.offsetToPos(expression.from).line + response.metadata.end_line - 1;
            insert_pos.ch = editor.getLine(insert_pos.line).length;
        }

        // insert result at the end of the expression.
        editor.replaceRange(insert_content, insert_pos);
        editor.setCursor(editor.offsetToPos(editor.posToOffset(insert_pos) + insert_content.length));
    }

    protected async create_args_payload(expression: Expression, app: App, view: MarkdownView): Promise<EvalArgsPayload> {
        return new EvalArgsPayload(expression.contents, LmatEnvironment.fromMarkdownView(app, view));
    }
    
    private evaluate_mode: string;
}