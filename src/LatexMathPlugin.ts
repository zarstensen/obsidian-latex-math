import { FileSystemAdapter, MarkdownView, Notice, Plugin } from 'obsidian';
import path from 'path';
import { EvaluateCommand } from '/controllers/commands/EvaluateCommand';
import { LatexMathCommand } from '/controllers/commands/LatexMathCommand';
import { SolveCommand } from '/controllers/commands/SolveCommand';
import { ConvertSympyCommand } from '/controllers/commands/ConvertSympyCommand';
import { TruthTableCommand } from '/controllers/commands/TruthTableCommand';
import { UnitConvertCommand } from '/controllers/commands/UnitConvertCommand';
import { HandlerInterrupter } from '/services/HandlerInterrupter';
import { CasClientExtractor } from '/models/cas/LmatCasClientExtractor';
import { ExecutableSpawner, SourceCodeSpawner } from '/models/cas/LmatCasClientSpawner';
import { CasServer, ClientResponse, UnixTimestampMillis } from '/models/cas/LmatCasServer';
import { LmatCodeBlockRenderer } from '/views/LmatCodeBlockRenderer';
import { LmatSettingsTab } from '/views/LmatSettingsTab';
import { EvaluateStatusBar } from '/views/LmatStatusBar';
import { ConfirmModal } from '/views/modals/ConfirmModal';
import { SuccessResponseVerifier } from '/models/cas/ResponseVerifier';
import { EvaluateMode } from '/models/cas/messages/EvaluateMessage';
import { TruthTableFormat } from '/models/cas/messages/TruthTableMessage';
import { CasCommandRequester } from './services/CasCommandRequester';
import { SymbolSetMessage } from './models/cas/messages/SymbolSetsMessage';

interface LatexMathPluginSettings {
    dev_mode: boolean;
}

const DEFAULT_SETTINGS: LatexMathPluginSettings = {
    dev_mode: false
};

declare global {
    const MathJax: any;
}

export default class LatexMathPlugin extends Plugin {
    settings: LatexMathPluginSettings;

    async onload() {
        console.log(`Loading Latex Math (v${this.manifest.version})`);

        if (!this.manifest.dir) {
            new Notice("Latex Math could not determine its plugin directory, aborting load.");
            return;
        }

        // require physics package
		// TODO: this should definetly not be here, but the plugin-refactor branch moves everything around anyways, so this may aswell be fixed there.

        const require_physics = "\\require{physics}";

        if (MathJax.tex2chtml == undefined) {
            MathJax.startup.ready = () => {
                MathJax.startup.defaultReady();
                MathJax.tex2chtml(require_physics);
            };
        } else {
            MathJax.tex2chtml(require_physics);
        }

        await this.loadSettings();
        this.addSettingTab(new LmatSettingsTab(this.app, this));

        this.setupCasConnection();

        const response_verifier = new SuccessResponseVerifier();

        response_verifier.onVerifyFailure(this.onCommandFailed);

        await this.setupStatusBar(new HandlerInterrupter(this.cas_server, response_verifier));


        // add code block renderer
        const lmat_code_block_renderer = new LmatCodeBlockRenderer(
            new CasCommandRequester(this.cas_server, this.spawn_cas_client_promise, response_verifier, SymbolSetMessage)
        );

        this.registerMarkdownCodeBlockProcessor("lmat", lmat_code_block_renderer.getHandler());

        // add commands
        this.addCommands(new Map([
            [new EvaluateCommand(EvaluateMode.EVAL, response_verifier), 'Evaluate LaTeX expression'],
            [new EvaluateCommand(EvaluateMode.EVALF, response_verifier), 'Evalf LaTeX expression'],
            [new EvaluateCommand(EvaluateMode.EXPAND, response_verifier), 'Expand LaTeX expression'],
            [new EvaluateCommand(EvaluateMode.FACTOR, response_verifier), 'Factor LaTeX expression'],
            [new EvaluateCommand(EvaluateMode.APART, response_verifier), 'Partial fraction decompose LaTeX expression'],
            [new SolveCommand(response_verifier), 'Solve LaTeX expression'],
            [new ConvertSympyCommand(response_verifier), 'Convert LaTeX expression to Sympy'],
            [new UnitConvertCommand(response_verifier), 'Convert units in LaTeX expression'],
            [new TruthTableCommand(TruthTableFormat.MARKDOWN, response_verifier), 'Create truth table from LaTeX expression (Markdown)'],
            [new TruthTableCommand(TruthTableFormat.LATEX_ARRAY, response_verifier), 'Create truth table from LaTeX expression (LaTeX)'],
        ]));
    }

    // sets up the given map of commands as obsidian commands.
    // the provided values for each command will be set as the command description.
    addCommands(commands: Map<LatexMathCommand, string>) {
        commands.forEach((description, cmd) => {

            this.addCommand({
                id: cmd.id,
                name: description,
                editorCallback: async (e, v) => {
                    await this.spawn_cas_client_promise;
                    cmd.functionCallback(this.cas_server, this.app, e, v as MarkdownView);
                }
            });
        });
    }

    onunload() {
        this.cas_server.shutdown(LatexMathPlugin.CAS_CLIENT_SHUTDOWN_TIMEOUT);
    }

    async loadSettings() {
        this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    }

    async saveSettings() {
        await this.saveData(this.settings);
    }

    private static readonly ERR_NOTICE_TIMEOUT = 30 * 1000;
    private static readonly ERR_NOTICE_LINE_COUNT = 8;
    private static readonly CAS_CLIENT_SHUTDOWN_TIMEOUT = 30;
    private static readonly STATUS_BAR_UPDATE_FREQ: UnixTimestampMillis = 500;
    private static readonly STATUS_BAR_MESSAGE_HANG_TIME: UnixTimestampMillis = 1000;

    private cas_server: CasServer;
    private spawn_cas_client_promise: Promise<void>;
    private prev_err_notice: Notice | null = null;

    private async setupCasConnection() {
        this.cas_server = new CasServer();
        this.cas_server.onError(this.handleCasError.bind(this));

        this.spawn_cas_client_promise = this.spawnCasClient(this.manifest.dir as string);
        this.spawn_cas_client_promise.catch((err) => {
            new Notice(`Latex Math could not start the cas client, aborting load.\n${err.message}`);
            throw err;
        });

        await this.spawn_cas_client_promise;
    }


    private async setupStatusBar(handler_interrupter: HandlerInterrupter): Promise<EvaluateStatusBar> {
        const status_bar = new EvaluateStatusBar(await this.addStatusBarItem());

        status_bar.show(false);

        window.setInterval(() => {
            status_bar.updateData({
                running_command_handlers: this.cas_server.getCurrentMessages().length
            });

            status_bar.show(this.cas_server.getHangingMessages({ min_hang_time: LatexMathPlugin.STATUS_BAR_MESSAGE_HANG_TIME }).length > 0);
        }, LatexMathPlugin.STATUS_BAR_UPDATE_FREQ);

        status_bar.onStatusBarClicked((_) => {
            new ConfirmModal(
                this.app,
                "Interrupt Evaluations",
                `Do you want to interrupt the ${this.cas_server.getCurrentMessages().length} hanging expression evaluation(s?)`,
                async () => {
                    await handler_interrupter.interruptAllHandlers();
                    new Notice("Successfully Interrupted Hanging Evaluations");
                }
            ).open();
        });

        return status_bar;
    }

    private async spawnCasClient(plugin_dir: string) {
        if (!(this.app.vault.adapter instanceof FileSystemAdapter)) {
            throw new Error(`Expected FileSystemAdapter, got ${this.app.vault.adapter}`);
        }
        const file_system_adapter: FileSystemAdapter = this.app.vault.adapter;

        const full_plugin_dir = path.join(file_system_adapter.getBasePath(), plugin_dir);
        const asset_extractor = new CasClientExtractor(full_plugin_dir);

        const cas_client_spawner = this.settings.dev_mode ? new SourceCodeSpawner(full_plugin_dir) : new ExecutableSpawner(asset_extractor);

        await this.cas_server.initializeAsync(cas_client_spawner);
    }

    private onCommandFailed(failed_command: LatexMathCommand, unexpected_response: ClientResponse, expected_statuses: Set<string>) {
        console.error("Command Failed!\nCommand:\t\t\t",
            failed_command,
            "\nExpected value types:\t",
            expected_statuses,
            "\nResponse:\t\t\t",
            unexpected_response
        );

        new Notice("An unexpected error occured whilst handling command.\nPlease see the dev console for more info\n(ctrl + shift + i)");
    }

    private handleCasError(usr_error: string, _dev_error: string): void {
        if (this.prev_err_notice !== null) {
            this.prev_err_notice.hide();
        }

        // limit error message to ERR_NOTICE_LINE_COUNT lines,
        // need to check the developer console to see the full message.

        const errorLines = usr_error.split('\n');
        const truncatedError = errorLines
            .slice(0, LatexMathPlugin.ERR_NOTICE_LINE_COUNT)
            .join('\n') +
            (errorLines.length > LatexMathPlugin.ERR_NOTICE_LINE_COUNT ? '\n...' : '') +
            "\n\nOpen the dev console for more info (ctrl + shift + i).";

        const err_notice = new Notice("Latex Math Error\n", LatexMathPlugin.ERR_NOTICE_TIMEOUT);

        const err_elem = err_notice.messageEl.createEl('code');
        err_elem.innerText = truncatedError;
        err_notice.messageEl.appendChild(err_elem);

        this.prev_err_notice = err_notice;
    }
}
