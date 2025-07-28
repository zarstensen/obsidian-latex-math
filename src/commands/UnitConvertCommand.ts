import { App, MarkdownView } from "obsidian";
import { EvalArgsPayload, EvaluateCommand, Expression } from "./EvaluateCommand";
import { UnitConvertModeModal } from "src/UnitConvertModeModal";
import { LmatEnvironment } from "src/LmatEnvironment";
import { LatexMathCommand } from "./LatexMathCommand";

class UnitConvertArgsPayload extends EvalArgsPayload {
    public constructor(
        expression: string,
        environment: LmatEnvironment,
        public target_units: string[]
    ) { super(expression, environment); }
}

export class UnitConvertCommand extends EvaluateCommand {
    public constructor(...args: ConstructorParameters<typeof LatexMathCommand>) {
        super('convert-units', ...args);
    }
    
    protected override async create_args_payload(expression: Expression, app: App, view: MarkdownView): Promise<EvalArgsPayload> {
        const modal = new UnitConvertModeModal(app);
        modal.open();
        const target_units = await modal.get_target_units();

        return new UnitConvertArgsPayload(expression.contents, LmatEnvironment.fromMarkdownView(app, view), target_units);
    }
}