import { App, Editor, MarkdownView, Notice } from "obsidian";
import { GenericPayload, StartCommandMessage, SuccessResponse, CasServer } from "src/LmatCasServer";
import { LatexMathCommand } from "./LatexMathCommand";
import { EquationExtractor } from "src/EquationExtractor";
import { LmatEnvironment } from "src/LmatEnvironment";

class SympyConvertArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
    ) { }
    [x: string]: unknown;
}

interface SympyConvertResponse {
    code: string;
}

export class SympyConvertCommand extends LatexMathCommand {
    readonly id: string = 'convert-to-sympy';

    public constructor(...base_args: ConstructorParameters<typeof LatexMathCommand>) {
        super(...base_args);
    }

    async functionCallback(cas_server: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        let equation: { from: number, to: number, block_to: number, contents: string } | null = null;
        
        // Extract equation to evaluate
        if(editor.getSelection().length <= 0) {
            equation = EquationExtractor.extractEquation(editor.posToOffset(editor.getCursor()), editor);
        } else {
            equation = {
              from: editor.posToOffset(editor.getCursor('from')),
              to: editor.posToOffset(editor.getCursor('to')),
              block_to: editor.posToOffset(editor.getCursor('to')),
              contents: editor.getSelection()  
            } ;
        }

        if (equation === null) {
            new Notice("You are not inside a math block");
            return;
        }

        const response = await cas_server.send(new StartCommandMessage({
            command_type: "convert-sympy",
            start_args: new SympyConvertArgsPayload(equation.contents, LmatEnvironment.fromMarkdownView(app, view))
        }));

        const result = this.response_verifier.verifyResponse<SympyConvertResponse>(response);

        // place the convertet python code into a code block right below the math block.

        const sympy_code_block = "\n```python\n" + result.code + "\n```\n";

        editor.replaceRange(sympy_code_block, editor.offsetToPos(equation.block_to));
        editor.setCursor(editor.offsetToPos(equation.to + sympy_code_block.length));
    }
    
}