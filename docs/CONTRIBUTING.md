# Contributin To The LaTeX Math Plugin

Planning to make a contribution to this plugin? If so, please make sure to check-out and make PR's to the `dev` branch.

The only exception to this are hotfixes, which should be merged into `main`.

Want to make changes to UI / UX? Checkout the `src` folder for the obsidian plugin.

Want to expand upon the CAS features of this plugin? Checkout the `lmat-cas-client` folder for the cas clients source code.

The following sections describe how to set up a development environment for **LaTeX Math**.
Make sure to have python (for cas client development) and / or NPM (for obsidian plugin development) installed before continuing.

### Developing the CAS Client

Start of with running the `setup-dev-env` python script from the root directory.

```sh
python setup-dev-env.py
```

This creates a virtual environment named `.venv` installed with all required dependencies. Furthermore, it sets up a git pre-push hook, which runs the entire test suite, before pushing.

To use this development environment in Obsidian, go to the **LaTeX Math** settings in the vault this repo has been cloned to, and toggle the `Developer Mode` switch to on. Make sure to reload the vault after doing this.

The plugin should now use the python source files and the created virtual environment, instead of the auto installed `lmat-cas-client` binary.

Any changes to the python source code requires reloading Obsidian to have any effect.

> [!CAUTION]
> If you are using VS Code as an IDE, make sure to add `push` as an entry to `git.commandsToLog` in VS Code (user or workspace), if you want to see the output of the push hook if it fails.

### Developing the Obsidian Plugin

Start out by downloading the [`bundle-bin.zip`](https://github.com/zarstensen/obsidian-latex-math/releases/latest) file from the latest release, and extract it in the root directory.

Now run `npm -i` still in the root directory.

To start auto building the project on any source code change, run `npm run dev`.
To perform a one-time production ready build, run `npm run build`.