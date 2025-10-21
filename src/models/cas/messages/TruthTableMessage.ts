import { GenericPayload, StartCommandMessage } from "../LmatCasServer";
import { LmatEnvironment } from "../LmatEnvironment";

// Enum of all possible truth table formats returned by the cas client
export enum TruthTableFormat {
    // truth table contents is formatted as a markdown table with latex entries.
    MARKDOWN = "md",
    // truth table is formatted in a latex array, displayable by mathjax 
    LATEX_ARRAY = "latex-array",
    // TODO: LATEX_TABLE?
    // this is not supported by mathjax, but could be usefull for real latex documents?
}

export class TruthTableArgsPayload implements GenericPayload {
    public constructor(
        public expression: string,
        public environment: LmatEnvironment,
        public truth_table_format: TruthTableFormat
    ) { }
    [x: string]: unknown;
}

export class TruthTableMessage extends StartCommandMessage {
    public constructor(args: TruthTableArgsPayload) {
        super({ command_type: 'truth-table', start_args: args });
    }
}

export interface TruthTableResponse {
    truth_table: string
}

