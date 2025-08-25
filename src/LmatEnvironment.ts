import { App, Editor, EditorPosition, MarkdownView } from "obsidian";
import * as toml from "toml";

type Definition = { name_expr: string, value_expr: string };

// The LmatEnvironment class represents an environment detailing how mathematical expressions,
// should be evaluated.
// it contains information about symbol assumptions, variable definitions, units, and solution domains.
export class LmatEnvironment {

    public static fromCodeBlock(code_block: string | undefined, definitions: Definition[]) {
        if(!code_block) {
            return new LmatEnvironment({}, definitions);
        }

        const parsed_lmat_block = toml.parse(code_block);

        return new LmatEnvironment(
            parsed_lmat_block.symbols,
            definitions,
            parsed_lmat_block.units?.system,
            parsed_lmat_block.domain?.domain
        );
    }

    // construct an LmatEnvironment class from the given active document, and cursor position.
    // this environment is constructed based on the closest lmat code block to the cursor (ignoring any blocks after the cursor).
    // variables are parsed from the text between the code block and the cursor.
    public static fromMarkdownView(app: App, markdown_view: MarkdownView, position?: EditorPosition): LmatEnvironment {
        // start by finding all lmat code blocks.
        position ??= markdown_view.editor.getCursor();

        if (!markdown_view.file) {
            throw new Error("No file found in the given markdown view");
        }

        let sections = app.metadataCache.getFileCache(markdown_view.file)?.sections;

        if (!sections) {
            throw new Error("No sections found in the given file");
        }

        const editor = markdown_view.editor;

        // filter out any non lmat code block sections
        sections = sections
            .filter((section) => section.type === "code")
            .filter((section) => {
                const code_block_contents = editor.getRange(editor.offsetToPos(section.position.start.offset), editor.offsetToPos(section.position.end.offset));
                return this.LMAT_BLOCK_REGEX.test(code_block_contents);
            });
        
        // find the closest lmat code block

        let closest_section = undefined;

        for(const section of sections) {
            if(section.position.end.offset < editor.posToOffset(position)) {
                closest_section = section;
            } else {
                break;
            }
        }

        if(!closest_section) {
            return new LmatEnvironment(undefined, this.parseDefinitions(editor.offsetToPos(0), position, editor));
        }

        // now generate lmat environment based on section contents.

        const lmat_block = editor.getRange(editor.offsetToPos(closest_section.position.start.offset), editor.offsetToPos(closest_section.position.end.offset));
        const lmat_block_content = lmat_block.match(this.LMAT_BLOCK_REGEX)?.[1];
        const definitions = this.parseDefinitions(editor.offsetToPos(closest_section.position.end.offset), position, editor);

        return LmatEnvironment.fromCodeBlock(lmat_block_content, definitions);
    }

    // regex for extracting the contents of an lmat code block.
    private static readonly LMAT_BLOCK_REGEX = /^```lmat\s*(?:\r\n|\r|\n)([\s\S]*?)```$/;

    private static readonly LMAT_DEFINITION_REGEX = /(?<!\\)(?:\\{2})*\$(?<definition_name>(?:(?<!\\)\\(?:\\{2})*\$|[^$])*):=(?<definition_expr>.*?)(?<!\\)(?:\\{2})*\$/gs; 

    private constructor(
        /**
         * symbols is a map of a symbols name and a list of all the assumptions,
         * which sympy will take into account when evaluating any expression, containing this symbol.
         */
        public symbols: { [symbol: string]: string[] } = {},
        public definitions: Definition[] = [],
        /**
         * the unit system to use when converting between units.
         * if left undefined, SI is used as the default system.
         */
        public unit_system: string | undefined = undefined,
        /**
         * the domain is a sympy expression, evaluating to the default solution domain of any equation solutions.
         */
        public domain: string | undefined = undefined
    ) { }

    private static parseDefinitions(from: EditorPosition, to: EditorPosition, editor: Editor) {
        const definitions: Definition[] = [ ];

        const search_range = editor.getRange(from, to);
        const definition_matches = search_range.matchAll(this.LMAT_DEFINITION_REGEX);

        for(const def of definition_matches) {
            const def_name = (def.groups?.definition_name ?? "").trim();
            const def_expr = (def.groups?.definition_expr ?? "").trim();

            if(def_name === "" || def_expr === "") {
                continue;
            }

            definitions.push({ name_expr: def_name, value_expr: def_expr });
        }

        return definitions;
    }
}