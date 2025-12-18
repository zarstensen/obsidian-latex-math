
<!-- omit in toc -->
# Contributing To The LaTeX Math Plugin

Planning to contribute to this plugin? If so, please make sure to checkout and make PRs to the **dev** branch.

The only exception is hotfixes, which should be branched from and merged into **main**.

## Development Environment Setup

The following sections describe how to set up a development environment for **LaTeX Math**.

Make sure to have [python 3.12 or later](https://www.python.org/) and [node + npm](https://nodejs.org/en/download/) installed before continuing.

<!-- omit in toc -->
## Table of Contents

- [Development Environment Setup](#development-environment-setup)
  - [Python Environment](#python-environment)
  - [Node Environment](#node-environment)
- [Tests and Code Quality](#tests-and-code-quality)
  - [Tests](#tests)
  - [Code Quality](#code-quality)
- [Developing](#developing)
  - [Adding Commands](#adding-commands)
  - [Extending The LaTeX Parser](#extending-the-latex-parser)
  - [Modifying The UX / UI](#modifying-the-ux--ui)

### Python Environment

Start by running the `setup-dev-env` Python script from the repository root.

This sets up a virtual environment with all required production and development dependencies.

```sh
python setup-dev-env.py
```

To use this development environment in Obsidian, go to the **LaTeX Math** settings in the vault where this repo has been cloned, and toggle the `Developer Mode` switch on. Reload the vault after doing this.

The plugin will now use the Python source files and the created virtual environment instead of the auto-installed `lmat-cas-client` binary.

Any changes to the Python source code require reloading Obsidian to take effect.

### Node Environment

Start out by downloading the [`bundle-bin.zip`](https://github.com/zarstensen/obsidian-latex-math/releases) file from the latest release (including beta releases), and extract it in the root directory.[^bundle-bin]

[^bundle-bin]: The exact contents of this folder do not matter as long as `Developer Mode` is on, but esbuild needs them to be present, otherwise dev builds will error out.

Now run `npm ci` in the root directory.

```sh
npm ci
```

This installs all needed dependencies for developing the Obsidian plugin.
It also sets up pre-push hooks that run all test suites.
To push to origin without executing the pre-push hook, use `git push --no-verify`.

> [!CAUTION]
> The pre-push hook does not work if `git push` is executed while inside a Python virtual environment.
>
> Run `git push` outside any Python virtual environment, or use `git push --no-verify` instead.

> [!CAUTION]
> If you use VS Code as an IDE, add `push` to `git.commandsToLog` (user or workspace) if you want to see the output of the push hook when it fails.

To start auto-building the project on any source code change, run `npm run dev`.

```sh
npm run dev
```

To perform a one-time production ready build, run `npm run build`.

```sh
npm run build
```

## Tests and Code Quality

### Tests

This project uses two testing frameworks: [pytest](https://docs.pytest.org/en/stable/) for the CAS client and [vitest](https://vitest.dev/) for the plugin codebase.

To run the entire test suite, execute the two commands below while inside the Python environment.

```sh
pytest
npm run test
```

### Code Quality

This project uses [ruff](https://docs.astral.sh/ruff/) for basic code quality checks.

Currently, only checks for redundant whitespace are included.

Use `ruff check` for a status report on code quality issues.

Use `ruff check --fix --preview` to automatically fix code quality issues.

## Developing

The following sections will provide a brief overview of parts of the codebase for common feature additions / changes.

In general, make sure to look around at similar and relevant code when planning how to implement your feature.

This will give a good understanding of how the code currently works, as well as how your code is expected to be implemented.

Make sure to add tests for any new features, if they are testable by 1 of the 2 test frameworks.

### Adding Commands

First, implement the command under `lmat-cas-client/lmat_cas_client/command_handlers`. This should handle the core CAS logic (the math goes here).
This file should also provide an interface for the command message (input) and the command result (output).

Register the command in `lmat-cas-client/lmat-cas-client.py` by calling ``client.register_handler`.

Add relevant message, payload, and response interfaces in `src/cas/messages`; these should correspond 1:1 with the message and result interface added in `lmat-cas-client`.

Add a new plugin command under `src/cas/commands`. This handles user interaction with the command as well as insertion of the result.

Register the command in `src/LatexMathPlugin.ts` as an argument to the `this.addCommands` call in the `onLoad` method.

### Extending The LaTeX Parser

The LaTeX parser is implemented with the [lark](https://lark-parser.readthedocs.io/en/latest/philosophy.html) library.

Start by looking at the [SYNTAX](SYNTAX.md) document to get a broad overview of the LaTeX syntax,
then dive deeper into `lmat-cas-client/lmat_cas_client/compiling/parsing/latex_math_grammar.lark` and the [lark documentation](https://lark-parser.readthedocs.io/en/latest/how_to_use.html) to understand the parser.

Transformers can be added or modified at `lmat-cas-client/lmat_cas_client/compiling/transforming`.

### Modifying The UX / UI

The plugin source (`src` folder) primarily handles UI / UX.

`lmat-cas-client` **ONLY** has to do with the core CAS logic, so no UI / UX goes on here.
Same with `src/cas`.
