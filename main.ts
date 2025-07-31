import { FileSystemAdapter, MarkdownView, Notice, Plugin, setIcon, setTooltip } from 'obsidian';
import { ClientResponse, CasServer, SuccessResponse, InterruptHandlerMessage } from 'src/LmatCasServer';
import { ExecutableSpawner, SourceCodeSpawner } from 'src/LmatCasClientSpawner';
import { LmatSettingsTab } from 'src/LmatSettingsTab';
import { LatexMathCommand } from 'src/commands/LatexMathCommand';
import { EvaluateCommand } from 'src/commands/EvaluateCommand';
import { SolveCommand } from 'src/commands/SolveCommand';
import { SympyConvertCommand } from 'src/commands/SympyConvertCommand';
import { UnitConvertCommand } from 'src/commands/UnitConvertCommand';
import { CasClientExtractor } from 'src/LmatCasClientExtractor';
import path from 'path';
import { TruthTableCommand, TruthTableFormat } from 'src/commands/TruthTableCommand';
import { SuccessResponseVerifier } from 'src/ResponseVerifier';
import { LmatCodeBlockRenderer } from 'src/LmatCodeBlockRenderer';
import { EvaluateStatusBar } from 'src/LmatStatusBar';
import { ConfirmModal } from 'src/modals/ConfirmModal';
import { InterruptCommand } from 'src/commands/InterruptCommand';

interface LatexMathPluginSettings {
    dev_mode: boolean;
}

const DEFAULT_SETTINGS: LatexMathPluginSettings = {
    dev_mode: false
};

export default class LatexMathPlugin extends Plugin {
    settings: LatexMathPluginSettings;

    async onload() {
        console.log(`Loading Latex Math (v${this.manifest.version})`);
        
        if(!this.manifest.dir) {
            new Notice("Latex Math could not determine its plugin directory, aborting load.");
            return;
        }
        
        await this.loadSettings();
        this.addSettingTab(new LmatSettingsTab(this.app, this));

        this.setupCasConnection();
        const response_verifier = new SuccessResponseVerifier();

        response_verifier.onVerifyFailure(this.onCommandFailed);

        const status_bar = new EvaluateStatusBar(await this.addStatusBarItem());
        status_bar.onStatusBarClicked((_) => { new ConfirmModal(this.app, "Interrupt Evaluations", `Do you want to interrupt the ${this.cas_server.getCurrentMessages().length} hanging expression evaluation(s?)`, async () => { 
                    
            const interrupt_promises: Promise<SuccessResponse>[] = [];
    
            // go through all currently registered handlers and try to interrupt them.
            for(const handler_uid of this.cas_server.getCurrentMessages()) {
                interrupt_promises.push(this.cas_server.send(new InterruptHandlerMessage({
                    target_uid: handler_uid
                })));
            }
    
            for(const interrupt_promise of interrupt_promises) {
                response_verifier.verifyResponse(await interrupt_promise);
            }
    
            new Notice("Successfully Interrupted Hanging Evaluations");
         }).open(); });
        status_bar.show(false);

        // Run a function every 500 ms
        window.setInterval(() => {
            status_bar.updateData({
                running_command_handlers: this.cas_server.getCurrentMessages().length
            });

            status_bar.show(this.cas_server.getHangingMessages({min_hang_time: 1}).length > 0);
        }, 500);
        
        
        // add code block renderer
        const lmat_code_block_renderer = new LmatCodeBlockRenderer(this.cas_server, this.spawn_cas_client_promise, response_verifier);
        this.registerMarkdownCodeBlockProcessor("lmat", lmat_code_block_renderer.getHandler());

        // add commands
        this.addCommands(new Map([
            [ new EvaluateCommand("eval", response_verifier), 'Evaluate LaTeX expression' ],
            [ new EvaluateCommand("evalf", response_verifier), 'Evalf LaTeX expression' ],
            [ new EvaluateCommand("expand", response_verifier), 'Expand LaTeX expression' ],
            [ new EvaluateCommand("factor", response_verifier), 'Factor LaTeX expression' ],
            [ new EvaluateCommand("apart", response_verifier), 'Partial fraction decompose LaTeX expression' ],
            [ new SolveCommand(response_verifier), 'Solve LaTeX expression' ],
            [ new SympyConvertCommand(response_verifier), 'Convert LaTeX expression to Sympy' ],
            [ new UnitConvertCommand(response_verifier), 'Convert units in LaTeX expression' ],
            [ new TruthTableCommand(TruthTableFormat.MARKDOWN, response_verifier), 'Create truth table from LaTeX expression (Markdown)' ],
            [ new TruthTableCommand(TruthTableFormat.LATEX_ARRAY, response_verifier), 'Create truth table from LaTeX expression (LaTeX)' ],
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

        // Start the cas server <-> client message loop
        this.cas_server.receiveLoop().catch((err) => {
            new Notice(`Latex Math experienced an unexpected error.\n${err.message}`);
            throw err;
        });

    }

    private async spawnCasClient(plugin_dir: string) {
        if(!(this.app.vault.adapter instanceof FileSystemAdapter)) {
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
        if(this.prev_err_notice !== null) {
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