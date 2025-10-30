import { syntaxTree } from '@codemirror/language';
import { PluginValue, ViewPlugin, EditorView, ViewUpdate } from '@codemirror/view';
import { Tree } from '@lezer/common';
import { finishRenderMath, renderMath } from 'obsidian';

export class DefinitionsViewPlugin implements PluginValue {
    constructor(_view: EditorView) {
        
    }

    update(update: ViewUpdate) {
        console.log("VIEW UPDATED");
        if(update.geometryChanged) {
            this.updateMathBLocks(update.view);
        }
    }

    extractMathBlocks(view: EditorView, syntax_tree: Tree) {

        // select all math block elements
        const mjx_container_elements = Array.from(view.contentDOM.querySelectorAll<HTMLElement>(
                '.cm-embed-block.math > mjx-container.MathJax[display="true"]'
            ));

        if(mjx_container_elements.length <= 0) {
            return;
        }

        let curr_mjx_elem = mjx_container_elements[0];

        const {from, to} = view.visibleRanges[0];

        enum Mode {
            FIRST,
            LAST
        }

        let mode: Mode = Mode.FIRST;

        // For each math container element, find the corresponding markdown text

        syntax_tree.iterate({
            from: from,
            to: to,
            enter(node) {
                if (mode === Mode.FIRST) {
                    // handle FIRST mode
                } else if (mode === Mode.LAST) {
                    // handle LAST mode
                }
            }
        });

        // running time of this is n * m
        for (const mjx_element of Array.from(mjx_container_elements)) {
            // Find the parent cm-embed-block element
            const embedBlock = mjx_element.closest('.cm-embed-block.math');
            if (!embedBlock) continue;
            
            // Find the position in the document
            // TODO: ignore duplicate positions.
            const pos = view.posAtDOM(embedBlock);

            // ignore positions not in the visible range.
            for (const { from, to } of view.visibleRanges) {
                if (pos < from || to < pos) {
                    continue;
                }
            }
            
            let node_first: number | undefined = undefined;
            let node_last: number | undefined = undefined;

            syntax_tree.iterate({
                from: pos,
                enter(node) {
                    if(node_first !== undefined) {
                        return false;
                    }

                    if(node.type.name.contains('math-begin')) {
                        node_first = node.to;
                        return false;
                    }
                }
            });

            if (node_first === undefined) {
                continue;
            }

            syntax_tree.iterate({
                from: pos,
                enter(node) {
                    if(node_first === undefined ||node_last !== undefined) {
                        return false;
                    }

                    if(node.type.name.contains('math-end') && node.from > node_first) {
                        node_last = node.from;
                        return false;
                    }
                }
            });

            if (node_last === undefined) {
                continue;
            }

            console.log(node_first, node_last);
            console.log(view.state.doc.sliceString(node_first, node_last));
            
            // Try to find the math block node
            // It might be this node or a parent
            // let mathNode = node;
            // while (mathNode && !mathNode.type.name.includes('math')) {
            //     mathNode = mathNode.parent;
            // }
            
            // if (mathNode) {
            // // Get the text of the math block
            // const from = mathNode.from;
            // const to = mathNode.to;
            // const mathText = view.state.doc.sliceString(from, to);
            // console.log(from, to);
            // console.log("Math block text:", mathText);
            // }
        }
    }

    async updateMathBLocks(view: EditorView) {
        // in here, get all math interval nodes, remember, storing the node in 'each' calls should COPY as it is by reference by default.
        // check this first, but i beleive begin and end nodes are not guaranteed to contain pairs in the visible region, therefore if any pairs are missing their begin / end nodes,
        // start from them and iterate up / down until a corresponding pair is found.
        // finally, now we have a bunch of intervals representing all *visible* math blocks.
        // now use the below querySelectorAll, and view.posAtDom to check which elements should even be processed.
        // after this use some helper methods and some caching to extract the definition contents and final sympy evaluation result.
        
        // Use the syntax tree to find the math block node
        const tree = syntaxTree(view.state);
        // Debug: Pretty print the syntax tree
        const printTree = (node: any, indent = 0) => {
            const prefix = ' '.repeat(indent);
            console.log(`${prefix}Node: ${node.type.name} (${node.from}-${node.to})`);
            
            if (node.firstChild) {
                let child = node.firstChild;
                while (child) {
                    printTree(child, indent + 2);
                    child = child.nextSibling;
                }
            }
        };

        this.extractMathBlocks(view, tree);

        // console.log("Syntax Tree:");
        // printTree(tree.topNode);

        // const mjx_container_elements = view.contentDOM.querySelectorAll<HTMLElement>(':scope > .cm-embed-block.math > mjx-container.MathJax[display="true"]');
        

        // // For each math container element, find the corresponding markdown text
        // for (const mjx_element of Array.from(mjx_container_elements)) {
        //     // Find the parent cm-embed-block element
        //     const embedBlock = mjx_element.closest('.cm-embed-block.math');
        //     if (!embedBlock) continue;
            
        //     // Find the position in the document
        //     const pos = view.posAtDOM(embedBlock);
        //     console.log(pos);
            
        //     let node_first = undefined;
        //     let node_last = undefined;

        //     tree.iterate({
        //         from: pos - 1,
        //         to: pos + 1000,
        //         enter(node) {
        //             if(node_first !== undefined) {
        //                 return false;
        //             }

        //             if(node.type.name.contains('math-begin')) {
        //                 node_first = node.to;
        //                 return false;
        //             }
        //         }
        //     });

        //     tree.iterate({
        //         from: pos - 1,
        //         to: pos + 1000,
        //         enter(node) {
        //             if(node_last !== undefined) {
        //                 return false;
        //             }

        //             if(node.type.name.contains('math-end')) {
        //                 node_last = node.from;
        //                 return false;
        //             }
        //         }
        //     });

            

        //     console.log(node_first, node_last);
        //     console.log(view.state.doc.sliceString(node_first, node_last));
            
        //     // Try to find the math block node
        //     // It might be this node or a parent
        //     // let mathNode = node;
        //     // while (mathNode && !mathNode.type.name.includes('math')) {
        //     //     mathNode = mathNode.parent;
        //     // }
            
        //     // if (mathNode) {
        //     // // Get the text of the math block
        //     // const from = mathNode.from;
        //     // const to = mathNode.to;
        //     // const mathText = view.state.doc.sliceString(from, to);
        //     // console.log(from, to);
        //     // console.log("Math block text:", mathText);
        //     // }
        // }
        
    }
}

export const definitions_view_plugin = ViewPlugin.fromClass(DefinitionsViewPlugin);
