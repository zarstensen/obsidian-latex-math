import { finishRenderMath, MarkdownPostProcessorContext, renderMath } from "obsidian";
import { LmatEnvironment } from "./LmatEnvironment";
import { StartCommandMessage, CasServer, GenericPayload } from "./LmatCasServer";
import { SuccessResponseVerifier } from "./ResponseVerifier";

class SymbolSetArgsPayload implements GenericPayload {
    public constructor(
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}

interface SymbolSetResponse {
    symbol_sets: string
}

// LmatCodeBlockRenderer provides a render handler for the latex math codeblock type.
export class LmatCodeBlockRenderer {
    
    constructor(protected cas_server: CasServer, public response_verifier: SuccessResponseVerifier) { }

    public getHandler(): (source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext) => Promise<any> | void {
        return this.renderLmatCodeBlock.bind(this);
    }

    private async renderLmatCodeBlock(source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext): Promise<void> {
        // Add the standard code block background div,
        // to ensure a consistent look with other code blocks.
        const div = el.createDiv("HyperMD-codeblock HyperMD-codeblock-bg lmat-block-container-flair");
        // same goes with the code block flair
        const flair = div.createSpan("code-block-flair lmat-block-flair");
        flair.innerText = "Latex Math";
        div.appendChild(flair);

        el.appendChild(div);

        // retreive to be rendered latex from python.
        // TODO: make compatible with threaded stuff. also generally just clean this main file up please...
        const response = await this.cas_server.send(new StartCommandMessage({
            command_type: "symbolsets",
            start_args: new SymbolSetArgsPayload(LmatEnvironment.fromCodeBlock(source, {}, {}))
        }));

        const result = this.response_verifier.verifyResponse<SymbolSetResponse>(response);

        // render the latex.
        div.appendChild(renderMath(result.symbol_sets, true));
        finishRenderMath();
    }
}