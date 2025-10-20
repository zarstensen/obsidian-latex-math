import { App, Modal } from "obsidian";

// The BaseModal handles common functionality between the modals
export class BaseModal extends Modal {
    constructor(app: App) {
        super(app);

        this.scope.register([], 'Enter', (event) => {
            event.preventDefault();
            this.default_action();
        });
    }
    protected default_action: () => void;
}
