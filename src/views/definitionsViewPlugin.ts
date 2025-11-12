import { syntaxTree } from '@codemirror/language';
import { PluginValue, ViewPlugin, EditorView, ViewUpdate } from '@codemirror/view';
import { Tree } from '@lezer/common';
import { finishRenderMath, renderMath } from 'obsidian';
import { EquationExtractor } from '/utils/EquationExtractor';

export class DefinitionsViewPlugin implements PluginValue {

    // use this on the query for html elements to check if definition has been computed.
    // not relevant for result preview?
    private math_set: WeakSet<HTMLElement>;

    constructor(_view: EditorView) {
        console.log(_view.contentDOM);
        this.math_set = new WeakSet<HTMLElement>();
    }

    update(update: ViewUpdate) {
        // console.log("VIEW UPDATED");
        if (update.geometryChanged) {
            this.updateMathBLocks(update.view);
        }
    }

    extractMathBlocks(view: EditorView, syntax_tree: Tree) {
        // TODO:
        // how to cache preview [x]
        // how to insert definition preview [x]
        // how to extract latex from element [~]
        // how to get live preview [ ]
        // how to check if is definition [~]

        // select all math block elements
        const mjx_container_elements = Array.from(view.contentDOM.querySelectorAll<HTMLElement>(
            '.math > mjx-container.MathJax'
        ));

        console.log(mjx_container_elements);

        // well thats that solved then. (how to cache preview [WeakSet], how to insert definition preview, render math + append child on iterated HTMLElements)
        for (const e of mjx_container_elements) {
            if (!this.math_set.has(e)) {

                // first check if it should be disregarded
                // this does not work with callouts, but thats ok for now.

                const start = view.posAtDOM(e);
                const end = view.posAtDOM(e, 1);

                if (start == end) {
                    continue;
                }

                // cache this block, so we dont process it again.
                this.math_set.add(e);

                // it should not be disregarded, now print the latex

                console.log(view.state.doc.slice(start, end));

                // update the doc preview with some fancy new transparent latex.
                const math_preview = renderMath(`~ := ${view.posAtDOM(e) + 1} ~ `, false);
                // 10% transparent (90% opaque)
                math_preview.style.opacity = '0.5';

                // Or, if you meant 10% opaque (very transparent, 90% transparent):
                // math_preview.style.opacity = '0.1';
                e.appendChild(math_preview);
            }
        }

        finishRenderMath(); // THIS one is important.
    }
}

export const definitions_view_plugin = ViewPlugin.fromClass(DefinitionsViewPlugin);
