import { FileSystemAdapter, finishRenderMath, MarkdownPostProcessorContext, MarkdownView, Notice, Plugin, renderMath } from 'obsidian';
import { ClientResponse, SympyServer } from 'src/SympyServer';
import { LmatEnvironment } from 'src/LmatEnvironment';
import { ExecutableSpawner, SourceCodeSpawner } from 'src/SympyClientSpawner';
import { LatexMathSettingsTab } from 'src/LatexMathSettingsTab';
import { LatexMathCommand } from 'src/commands/LatexMathCommand';
import { EvaluateCommand } from 'src/commands/EvaluateCommand';
import { SolveCommand } from 'src/commands/SolveCommand';
import { SympyConvertCommand } from 'src/commands/SympyConvertCommand';
import { UnitConvertCommand } from 'src/commands/UnitConvertCommand';
import { SympyClientExtractor } from 'src/SympyClientExtractor';
import path from 'path';
import { TruthTableCommand, TruthTableFormat } from 'src/commands/TruthTableCommand';
import { SuccessResponseVerifier } from 'src/ResponseVerifier';
import { LmatCodeBlockRenderer } from 'src/LmatCodeBlockRenderer';

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

        await this.loadSettings();
        this.addSettingTab(new LatexMathSettingsTab(this.app, this));
        
        if(!this.manifest.dir) {
            new Notice("Latex Math could not determine its plugin directory, aborting load.");
            return;
        }

        this.sympy_evaluator = new SympyServer();

        // forward python errors directly to the user.
        this.sympy_evaluator.on_error((usr_error, _dev_error) => {
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
        });

        // Add commands

        const response_verifier = new SuccessResponseVerifier();

        response_verifier.onVerifyFailure(this.onCommandFailed);

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

        // spawn sympy client
        this.spawn_sympy_client_promise = this.spawnSympyClient(this.manifest.dir);
        this.spawn_sympy_client_promise.catch((err) => {
            new Notice(`Latex Math could not start the Sympy client, aborting load.\n${err.message}`);
            throw err;
        });
        
        (async() => {
            await this.spawn_sympy_client_promise;

            console.log(this.sympy_evaluator);

            const lmat_code_block_renderer = new LmatCodeBlockRenderer(this.sympy_evaluator, response_verifier);

            this.registerMarkdownCodeBlockProcessor("lmat", lmat_code_block_renderer.getHandler());
        })();

        // Start a background thread to repeatedly await receive
        const receiveLoop = async () => {
            await this.spawn_sympy_client_promise;
            // TODO: exit this on exit, also this should be its own function,a sl 
            while (true) {
            try {
                console.log("TRY RECEIVE");
                const response = await this.sympy_evaluator.receive();
                console.log("Received response from Sympy evaluator:", response);
            } catch (err) {
                console.error("Error in receive loop:", err);
                break; // Exit the loop on error
            }
            }
        };

        // Start the loop
        receiveLoop();
    }

    // sets up the given map of commands as obsidian commands.
    // the provided values for each command will be set as the command description.
    addCommands(commands: Map<LatexMathCommand, string>) {
        commands.forEach((description, cmd) => {
          
            this.addCommand({
                id: cmd.id,
                name: description,
                editorCallback: async (e, v) => { 
                    await this.spawn_sympy_client_promise;
                    cmd.functionCallback(this.sympy_evaluator, this.app, e, v as MarkdownView);
                }
            });
        });
    }

    onunload() {
        this.sympy_evaluator.shutdown(LatexMathPlugin.SYMPY_CLIENT_SHUTDOWN_TIMEOUT);
    }

    async loadSettings() {
        this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
    }

    async saveSettings() {
        await this.saveData(this.settings);
    }

    private static readonly ERR_NOTICE_TIMEOUT = 30 * 1000;
    private static readonly ERR_NOTICE_LINE_COUNT = 8;
    private static readonly SYMPY_CLIENT_SHUTDOWN_TIMEOUT = 30;

    private sympy_evaluator: SympyServer;
    private spawn_sympy_client_promise: Promise<void>;
    private prev_err_notice: Notice | null = null;

    private async spawnSympyClient(plugin_dir: string) {
        if(!(this.app.vault.adapter instanceof FileSystemAdapter)) {
            throw new Error(`Expected FileSystemAdapter, got ${this.app.vault.adapter}`);
        }
        const file_system_adapter: FileSystemAdapter = this.app.vault.adapter;

        const full_plugin_dir = path.join(file_system_adapter.getBasePath(), plugin_dir);
        const asset_extractor = new SympyClientExtractor(full_plugin_dir);

        // spawn sympy client process.
        const sympy_client_spawner = this.settings.dev_mode ? new SourceCodeSpawner(full_plugin_dir) : new ExecutableSpawner(asset_extractor);

        await this.sympy_evaluator.initializeAsync(sympy_client_spawner);
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
}