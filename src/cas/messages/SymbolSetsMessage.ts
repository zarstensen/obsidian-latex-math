import { GenericPayload, StartCommandMessage } from "../LmatCasServer";
import { LmatEnvironment } from "../LmatEnvironment";

export class SymbolSetArgsPayload implements GenericPayload {
    public constructor(
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}

export class SymbolSetMessage extends StartCommandMessage {
    public constructor(args: SymbolSetArgsPayload) {
        super({ command_type: 'symbolsets', start_args: args });
        
    }
}

export interface SymbolSetResponse {
    symbol_sets: string
}