import { CasServer, StartCommandMessage } from "/models/cas/LmatCasServer";
import { SuccessResponseVerifier } from "/models/cas/ResponseVerifier";

export class CasCommandRequester<TMsg extends StartCommandMessage, TArgs, TResponse> {
    constructor(
        private cas_server: CasServer,
        private spawn_cas_client_promise: Promise<void>,
        private response_verifier: SuccessResponseVerifier,
        private msg_ctor: new (args: TArgs) => TMsg,
    ) { }

    public async sendRequest(args: TArgs): Promise<TResponse> {
        await this.spawn_cas_client_promise;

        const message = new this.msg_ctor(args);
        const response = await this.cas_server.send(message).response;

        return this.response_verifier.verifyResponse<TResponse>(response);
    }
}
