import { setIcon, setTooltip } from "obsidian";

export interface EvaluateStatusBarData {
    running_command_handlers: number
}

import { EventEmitter } from "events";

export class EvaluateStatusBar {

    constructor(
        protected status_bar_el: HTMLElement
    ) {
        this.status_bar_el.addClass('mod-clickable');
        
        this.status_bar_el.onClickEvent((_) => {
            this.click_event_emitter.emit(this.CLICK_EVENT, this);
        });

        setIcon(this.status_bar_el.createEl('span', { cls: 'lmat-load-spin' }), 'loader-circle');
        this.status_bar_el.createEl('span', { cls: 'lmat-status-text', text: "evaluating" });

        this.updateData(this.data);
        this.show(false);
    }

    public updateData(new_data: EvaluateStatusBarData) {
        this.data = new_data;

        setTooltip(this.status_bar_el, `LaTeX Math is currently\nevaluating ${this.data.running_command_handlers} expression(s)`, { placement: 'top' });
    }

    public show(show: boolean) {
        if(show) {
            this.status_bar_el.style.display = '';
        } else {
            this.status_bar_el.style.display = 'none';
        }
    }

    public onStatusBarClicked(handler: (status_bar: EvaluateStatusBar) => void) {
        this.click_event_emitter.on(this.CLICK_EVENT, handler);
    }

    protected data: EvaluateStatusBarData = { 
        running_command_handlers: 0
    };

    protected readonly CLICK_EVENT: string = 'status-bar-clicked';
    protected click_event_emitter: EventEmitter = new EventEmitter();
}