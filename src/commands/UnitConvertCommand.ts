import { App, MarkdownView } from "obsidian";
import { EvaluateCommand, Expression } from "./EvaluateCommand";
import { UnitConvertModeModal } from "modals/UnitConvertModeModal";
import { LmatEnvironment } from "cas/LmatEnvironment";
import { LatexMathCommand } from "./LatexMathCommand";
import { EvaluateArgsPayload, EvaluateMode, UnitConvertArgsPayload } from "cas/messages/EvaluateMessage";

export class UnitConvertCommand extends EvaluateCommand {
    public constructor(...args: ConstructorParameters<typeof LatexMathCommand>) {
        super(EvaluateMode.CONVERT_UNITS, ...args);
    }
    
    protected override async createArgsPayload(expression: Expression, app: App, view: MarkdownView): Promise<EvaluateArgsPayload> {
        const modal = new UnitConvertModeModal(app);
        modal.open();
        const target_units = await modal.getTargetUnits();

        return new UnitConvertArgsPayload(expression.contents, LmatEnvironment.fromMarkdownView(app, view), target_units);
    }
}