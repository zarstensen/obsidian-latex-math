import { GenericPayload, StartCommandMessage } from "../../../services/CasServer";
import { LmatEnvironment } from "../LmatEnvironment";

export type LatexMathSymbol = { sympy_symbol: string, latex_symbol: string };

export class SolveArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
        public symbols: string[]
    ) { }
    [x: string]: unknown;
}

export class SolveMessage extends StartCommandMessage {
    constructor(args: SolveArgsPayload) {
        super({ command_type: 'solve', start_args: args });
    }
}

export interface SolveResponse {
    solution_set: string
}


export class SolveInfoArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}

export class SolveInfoMessage extends StartCommandMessage {
    public constructor(args: SolveInfoArgsPayload) {
        super({ command_type: 'solve-info', start_args: args });
    }
}

export interface SolveInfoResponse {
    required_symbols: number
    available_symbols: LatexMathSymbol[],
}
