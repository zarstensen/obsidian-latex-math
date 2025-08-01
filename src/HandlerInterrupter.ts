import { CasServer, InterruptHandlerMessage } from "./LmatCasServer";
import { SuccessResponseVerifier } from "./ResponseVerifier";

export class HandlerInterrupter {
    constructor(protected cas_server: CasServer, protected response_verifier: SuccessResponseVerifier)
    { }

    public async interruptAllHandlers(): Promise<void> {
        const response = await this.cas_server.send(new InterruptHandlerMessage({
                target_uids: this.cas_server.getCurrentMessages()
            }));
    
        this.response_verifier.verifyResponse(response);
    }
}