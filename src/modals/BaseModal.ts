import { App, Modal } from "obsidian";

// The UnitConvertModeModal provides a modal dialog to specify a list of units which should be converted to.
export class BaseModal extends Modal {
    constructor(app: App) {//, protected on_confirm: () => void) {
        super(app);

        this.scope.register(null, 'Enter', (event) => {
            event.preventDefault()
            this.on_confirm();
        });
    }
    protected on_confirm: () => void;
}
