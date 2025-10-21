import { GenericPayload, StartCommandMessage } from "../../LmatCasServer";

export class TestHangArgsPayload implements GenericPayload {
    public constructor(
        public hang_time: number
    ) { }
    [x: string]: unknown;
}

export class TestHangMessage extends StartCommandMessage {
    constructor(args: TestHangArgsPayload) {
        super({ command_type: 'test-hang', start_args: args });
    }
}

export type TestHangResult = Record<string, never>;
