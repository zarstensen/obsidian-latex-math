import { App, Editor, MarkdownView } from "obsidian";
import { SuccessResponseVerifier } from "../../models/cas/ResponseVerifier";
import { CasServer } from "/models/cas/LmatCasServer";

// Abstract class for a latex math command
// The id will be used to set the resulting obsidian command id.
// function callback is called whenever the command has been invoked by the user.
// use the response_verifire dependency to verify responses sent to the CasServer.
export abstract class LatexMathCommand {
    readonly id: string;

    constructor(public response_verifier: SuccessResponseVerifier) { }

    abstract functionCallback(cas_server: CasServer, app: App, editor: Editor, view: MarkdownView): Promise<void>; // Method to execute the command
}