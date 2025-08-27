import { finishRenderMath, MarkdownPostProcessorContext, renderMath } from "obsidian";
import { LmatEnvironment } from "./cas/LmatEnvironment";
import { CasServer } from "./cas/LmatCasServer";
import { SuccessResponseVerifier } from "./cas/ResponseVerifier";
import { SymbolSetArgsPayload, SymbolSetMessage, SymbolSetResponse } from "./cas/messages/SymbolSetsMessage";

// LmatCodeBlockRenderer provides a render handler for the latex math codeblock type.
export class LmatCodeBlockRenderer {
    
    constructor(protected cas_server: CasServer, protected spawn_cas_client_promise: Promise<void>, public response_verifier: SuccessResponseVerifier) { }

    public getHandler(): (source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext) => Promise<void> | void {
        return this.renderLmatCodeBlock.bind(this);
    }

    private async renderLmatCodeBlock(source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext): Promise<void> {
        await this.spawn_cas_client_promise;

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
        const response = await this.cas_server.send(new SymbolSetMessage(
            new SymbolSetArgsPayload(LmatEnvironment.fromCodeBlock(source, [ ]))
        )).response;

        const result = this.response_verifier.verifyResponse<SymbolSetResponse>(response);

        // render the latex.
        div.appendChild(renderMath(result.symbol_sets, true));
        finishRenderMath();
    }
}