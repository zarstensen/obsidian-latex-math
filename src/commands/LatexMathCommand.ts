import { App, Editor, MarkdownView } from "obsidian";
import { SuccessResponseVerifier } from "src/ResponseVerifier";
import { SympyServer } from "src/SympyServer";

// Interface for a latex math command
// The id will be used to set the resulting obsidian command id.
// function callback is called whenever the command has been invoked by the user.
export abstract class LatexMathCommand {
    readonly id: string;

    constructor(public response_verifier: SuccessResponseVerifier) { }

    abstract functionCallback(evaluator: SympyServer, app: App, editor: Editor, view: MarkdownView): Promise<void>; // Method to execute the command
}