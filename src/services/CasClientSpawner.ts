import { ChildProcessWithoutNullStreams, spawn } from "child_process";
import { join } from "path";
import { CasClientExtractor } from "./CasClientExtractor";

// Interface for spawning a cas client process.
export interface CasClientSpawner {
    spawnClient(port: number): Promise<ChildProcessWithoutNullStreams>
}

// Spawns a cas client process with python source files in the given virtual environment, with the given python executable.
export class SourceCodeSpawner implements CasClientSpawner {
    constructor(protected plugin_dir: string, protected python_exe = "python", protected venv = ".venv") { }

    public async spawnClient(port: number): Promise<ChildProcessWithoutNullStreams> {

        return spawn(join(this.plugin_dir, this.venv, process.platform === "win32" ? "Scripts" : "bin", this.python_exe), [join(this.plugin_dir, "lmat-cas-client/lmat-cas-client.py"), port.toString()]);
    }
}

// Spawns a cas client through a pyinstalled executable.
export class ExecutableSpawner implements CasClientSpawner {
    constructor(private asset_extractor: CasClientExtractor) { }

    public async spawnClient(port: number): Promise<ChildProcessWithoutNullStreams> {
        if (!(await this.asset_extractor.hasBundledClients())) {
            await this.asset_extractor.extractClients();
        }

        return spawn(this.asset_extractor.getCurrentOsClientPath(), [port.toString()]);
    }
}
