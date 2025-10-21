import { GenericPayload, StartCommandMessage } from "../LmatCasServer";
import { LmatEnvironment } from "../LmatEnvironment";

export class ConvertSympyArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
    ) { }
    [x: string]: unknown;
}

export class ConvertSympyMessage extends StartCommandMessage {
    constructor(args: ConvertSympyArgsPayload) {
        super({ command_type: 'convert-sympy', start_args: args });
    }
}

export interface ConvertSympyResponse {
    code: string;
}
