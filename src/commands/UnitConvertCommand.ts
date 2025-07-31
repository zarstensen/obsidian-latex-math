import { App, MarkdownView } from "obsidian";
import { EvaluateArgsPayload, EvaluateCommand, Expression } from "./EvaluateCommand";
import { UnitConvertModeModal } from "src/UnitConvertModeModal";
import { LmatEnvironment } from "src/LmatEnvironment";
import { LatexMathCommand } from "./LatexMathCommand";

class UnitConvertArgsPayload extends EvaluateArgsPayload {
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
    
    protected override async createArgsPayload(expression: Expression, app: App, view: MarkdownView): Promise<EvaluateArgsPayload> {
        const modal = new UnitConvertModeModal(app);
        modal.open();
        const target_units = await modal.getTargetUnits();

        return new UnitConvertArgsPayload(expression.contents, LmatEnvironment.fromMarkdownView(app, view), target_units);
    }
}