import { App, Editor, MarkdownView, Notice } from "obsidian";
import { CasServer, InterruptHandlerMessage, SuccessResponse } from "src/LmatCasServer";
import { LatexMathCommand } from "./LatexMathCommand";

export class InterruptCommand extends LatexMathCommand {
    readonly id: string = 'interrupt-handlers';
    
    public async functionCallback(cas_server: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void> {
        
        const interrupt_promises: Promise<SuccessResponse>[] = [];

        // go through all currently registered handlers and try to interrupt them.
        for(const handler_uid of cas_server.getCurrentMessages()) {
            interrupt_promises.push(cas_server.send(new InterruptHandlerMessage({
                target_uid: handler_uid
            })));
        }

        for(const interrupt_promise of interrupt_promises) {
            this.response_verifier.verifyResponse(await interrupt_promise);
        }

        new Notice("Successfully Interrupted Hanging Evaluations");
    }

}