import { CasServer, InterruptHandlerMessage } from "../models/cas/LmatCasServer";
import { SuccessResponseVerifier } from "/models/cas/ResponseVerifier";

// Class responsible for interrupting all hanging handlers of a given CasServer,
// verifying the interrupt message response with the given SuccessResponseVerifier.
export class HandlerInterrupter {
    constructor(protected cas_server: CasServer, protected response_verifier: SuccessResponseVerifier) { }

    public async interruptAllHandlers(): Promise<void> {
        const response = await this.cas_server.send(new InterruptHandlerMessage({
            target_uids: this.cas_server.getCurrentMessages()
        })).response;

        this.response_verifier.verifyResponse(response);
    }
}