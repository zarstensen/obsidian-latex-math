import { App, Modal, Setting } from "obsidian";

export class ConfirmModal extends Modal {
    constructor(app: App, title: string, prompt: string, protected on_confirm: () => void) {
        super(app);
        this.setTitle(title);

        new Setting(this.contentEl)
            .setDesc(prompt);

        new Setting(this.contentEl)
        .addButton((btn) => btn
                .setButtonText("Confirm")
                .setCta()
                .onClick(() => {
                    this.close();
                    on_confirm();
                })
        ).addButton((btn) => btn
                .setButtonText("Cancel")
                .onClick(() => {
                    this.close();
                })
        );
    }
}