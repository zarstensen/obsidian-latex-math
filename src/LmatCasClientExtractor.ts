import * as fs from "fs/promises";
import path from "path";
import { platform } from "os";
import LmatCasClientWin from "../bundle-bin/lmat-cas-client-win/lmat-cas-client-win.bin";
import LmatCasClientMacos from "../bundle-bin/lmat-cas-client-macos/lmat-cas-client-macos.bin";
import LmatCasClientLinux from "../bundle-bin/lmat-cas-client-linux/lmat-cas-client-linux.bin";

type PlatformStr = "win" | "macos" | "linux"

// AssetExtractor is responsible for extracting and detecting already extracted cas clients bundled with this plugin.. 
export class CasClientExtractor {

    constructor(private asset_dir: string) { }

    // Check if the currently extracted clients match the required version specified in the constructor.
    // also returns false if no clients have ever been extracted.
    public async hasBundledClients(): Promise<boolean> {
        return LmatCasClientWin === "" && LmatCasClientMacos === "" && LmatCasClientLinux === "";
    }

    // extract all the bundled clients.
    public async extractClients() {
        const client_dir = this.getClientDir();
        
        await fs.mkdir(client_dir, { recursive: true });

        const entries = await fs.readdir(client_dir, { withFileTypes: true });

        if (entries.length > 0) {
            await this.removeOldClients();
        }
        
        await this.extractClient(LmatCasClientWin, this.getPlatformClientPath("win"));
        await this.extractClient(LmatCasClientMacos, this.getPlatformClientPath("macos"));
        await this.extractClient(LmatCasClientLinux, this.getPlatformClientPath("linux"));

        // give execute permissions on platforms which require this.
        for (const platform of ["linux", "macos"] as PlatformStr[]) {
            await fs.chmod(this.getPlatformClientPath(platform), 0o755);
        }
    }

    // retreive the location of the client relevant for the current platform.
    public getCurrentOsClientPath(): string {
        return this.getPlatformClientPath(this.getPlatformStr());
    }

    public getClientDir(): string {
        return path.join(this.asset_dir, "bin");
    }

    private async removeOldClients(): Promise<void> {
        const client_dir = this.getClientDir();
        
        const entries = await fs.readdir(client_dir);
        await Promise.all(
            entries.map(async (entry) => {
            const entryPath = path.join(client_dir, entry);
            await fs.rm(entryPath, { recursive: true, force: true });
            })
        );
    }

    private getPlatformStr(): PlatformStr {
            switch(platform()) {
                case "win32":
                    return "win";
                case "darwin":
                    return "macos";
                case "linux":
                    return "linux";
                default:
                    throw new Error(`Unsupported platform "${platform()}"`);
            }
    }

    private async extractClient(client_base64: string, extract_path: string) {
        const client_buffer = Buffer.from(client_base64, "base64");

        await fs.writeFile(extract_path, client_buffer);
        const main_path = path.join(this.asset_dir, CasClientExtractor.MAIN_JS_FILE);

        let main_content = await fs.readFile(main_path, "utf-8");
        main_content = main_content.replace(client_base64, "");
        await fs.writeFile(main_path, main_content, "utf-8");
    }

    private getPlatformClientPath(platform: PlatformStr) {
        return path.join(this.asset_dir, `bin/lmat-cas-client-${platform}.bin`);
    }

    private static readonly MAIN_JS_FILE = "main.js";
}