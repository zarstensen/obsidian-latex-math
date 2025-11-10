import { GenericPayload, StartCommandMessage } from "../../../services/CasServer";
import { LmatEnvironment } from "../LmatEnvironment";

export enum EvaluateMode {
    EVAL = 'eval',
    EVALF = 'evalf',
    EXPAND = 'expand',
    FACTOR = 'factor',
    APART = 'apart',
    CONVERT_UNITS = 'convert-units'
}

export class EvaluateArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment
    ) { }
    [x: string]: unknown;
}


export class UnitConvertArgsPayload extends EvaluateArgsPayload {
    public constructor(
        expression: string,
        environment: LmatEnvironment,
        public target_units: string[]
    ) { super(expression, environment); }
}


export class EvaluateMessage extends StartCommandMessage {
    constructor(mode: EvaluateMode, args: EvaluateArgsPayload) {
        super({ command_type: mode.toString(), start_args: args });
    }
}

export interface EvaluateResponse {
    metadata: {
        separator: string,
        end_line: number
    },
    evaluated_expression: string
}
