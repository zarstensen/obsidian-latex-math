import { setIcon, setTooltip } from "obsidian";
import { EventEmitter } from "events";

export interface EvaluateStatusBarData {
    running_command_handlers: number
}

// EvaluateStatusBar manages an HTMLElement added with addStatusBarElement,
// which displays the current cas client evaluation status to the user.
export class EvaluateStatusBar  {

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

    // provide updated evaluate status data to the status bar.
    // this updates the visuals of the status bar from the new data.
    public updateData(new_data: EvaluateStatusBarData) {
        this.data = new_data;

        setTooltip(this.status_bar_el, `LaTeX Math is currently\nevaluating ${this.data.running_command_handlers} expression(s)`, { placement: 'top' });
    }

    // visually show or hide the status bar.
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