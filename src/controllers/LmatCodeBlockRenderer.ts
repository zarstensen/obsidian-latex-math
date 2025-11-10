import { finishRenderMath, MarkdownPostProcessorContext, renderMath } from "obsidian";
import { LmatEnvironment } from "models/cas/LmatEnvironment";
import { SymbolSetArgsPayload, SymbolSetMessage, SymbolSetResponse } from "models/cas/messages/SymbolSetsMessage";
import { CasCommandRequester } from "services/CasCommandRequester";

// LmatCodeBlockRenderer provides a render handler for the latex math codeblock type.
export class LmatCodeBlockRenderer {

    constructor(protected symbol_set_requester: CasCommandRequester<SymbolSetMessage, SymbolSetArgsPayload, SymbolSetResponse>) { }

    public getHandler(): (source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext) => Promise<void> | void {
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
        const result = await this.symbol_set_requester.sendRequest(
            new SymbolSetArgsPayload(LmatEnvironment.fromCodeBlock(source, []))
        );

        // render the latex.
        div.appendChild(renderMath(result.symbol_sets, true));
        finishRenderMath();
    }
}