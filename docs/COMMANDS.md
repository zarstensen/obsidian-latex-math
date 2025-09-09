
<!-- omit in toc -->
# LaTeX Math Commands

This documentation section provides detailed descriptions for all obsidian commands provided by the **LaTeX Math** plugin. For a quick overview, take a look at the [README command list](../README.md#command-list).

<!-- omit in toc -->
## Table Of Contents

- [General Information](#general-information)
- [Commands](#commands)
  - [Evaluate LaTeX Expression](#evaluate-latex-expression)
  - [Evalf LaTeX Expression](#evalf-latex-expression)
  - [Factor LaTeX Expression](#factor-latex-expression)
  - [Expand LaTeX Expression](#expand-latex-expression)
  - [Partial Fraction Decompose LaTeX Expression](#partial-fraction-decompose-latex-expression)
  - [Convert Units In LaTeX Expression](#convert-units-in-latex-expression)
  - [Solve LaTeX Expression](#solve-latex-expression)
  - [Create Truth Table from LaTeX Expression](#create-truth-table-from-latex-expression)
  - [Convert LaTeX Expression To Sympy](#convert-latex-expression-to-sympy)

## General Information

In general, all commands require a LaTeX expression as input.
The contents of the input are decided based on various conditions.
See the list below for a list of required conditions as well as the corresponding input, ordered by decreasing priority.

- **Selection is present:** Use selection as the input.
- **Cursor is inside a math block:**[^math-block] Use the contents of the math block as input.
- **Otherwise:** Input cannot be determined, show an error to the user.

[^math-block]: A math block is any text surrounded by unescaped dollar signs `$`.

If a command is being processed for longer than some set time (currently 1 sec), **LaTeX Math** will display a clickable 'evaluating' entry in the Obsidian status bar.

Upon clicking this, one gets the option to interrupt all currently processing commands.

This is especially useful if one accidentally tries to evaluate an intensive expression, which may never finish within a reasonable time frame.

## Commands

### Evaluate LaTeX Expression

> Obsidian command name: `Evaluate LaTeX expression`

The `Evaluate LaTeX expression` command simplifies (via. [`sympy.simplify`](https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html#simplify)) the *right most* expression in the given LaTeX input, and inserts the result to the right of the input, separated by `=`.

As an example, if `2x < y = 3^2` is the input, then **LaTeX Math** evaluates `3^2` (the *right most* expression) to be `9`, and inserts `= 9` at the end of the input.

If the input is a system of relations, then the *right most* expression of the *bottom most* line is evaluated and inserted on the same line.

### Evalf LaTeX Expression

> Obsidian command name: `Evalf LaTeX expression`

Same as [Evaluate LaTeX Expression](#evaluate-latex-expression), except [`sympy.evalf`](https://docs.sympy.org/latest/modules/core.html#module-sympy.core.evalf) is also applied to the parsed input, after simplification.

### Factor LaTeX Expression

> Obsidian command name: `Factor LaTeX expression`

Same as [Evaluate LaTeX Expression](#evaluate-latex-expression), except [`sympy.factor`](https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html#factor) is also applied to the parsed input, after simplification.

### Expand LaTeX Expression

> Obsidian command name: `Expand LaTeX expression`

Same as [Evaluate LaTeX Expression](#evaluate-latex-expression), except [`sympy.expand`](https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html#expand) is also applied to the parsed input, after simplification.

### Partial Fraction Decompose LaTeX Expression

> Obsidian command name: `Partial Fraction Decompose LaTeX expression`

Same as [Evaluate LaTeX Expression](#evaluate-latex-expression), except [`sympy.apart`](https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html#apart) is also applied to the parsed input, after simplification.

### Convert Units In LaTeX Expression

> Obsidian command name: `Partial Fraction Decompose LaTeX expression`

This command prompts for a list of units[^unit-list] separated by whitespace which existing units should be converted to.

[^unit-list]: see [SYNTAX.md] for a list of units.

Upon confirmation of the unit list, this command parses and evaluates the LaTeX input like the [Evaluate LaTeX Expression](#evaluate-latex-expression) command, and performs the unit conversion on the simplified result.

> [!NOTE]
> **Example**
>
> Supplied list of units through the unit modal is `km h`, this is interpreted as the units `km` and `h`
>
> LaTeX input is `50 \frac{{m}}{{s}}`.
>
> Output is `180 \frac{{km}}{{h}}`.

### Solve LaTeX Expression

> Obsidian command name: `Solve LaTeX expression`

This command attempts to parse a single or a series of equations.

The output is always placed in a `$$ ... $$` math block, below the LaTeX input.

If there are too many unknowns to solve for, **LaTeX Math** prompts the user to select which symbols should be solved for.

One can also specify the *solution domain* for single equations.

Series of equations can be notated by chaining multiple relations together (`x < y < z`) or by inserting multiple relations in a `cases` or `align` environment (`\begin{cases} x = 2 y \\ y = 5 \end{cases}`).

#### Restricting the solution

The method for restricting the set of solutions for a given input varies on the input type.

If the input is a single relation, then one must restrict the solution set either through the solve modals `Solution domain` input,
or in the `lmat` environments [domain field](MISSING LINK).

If the input is a series of relations, one must restrict the solution set by applying [assumptions on the unknown variables](MISSING LINK) in the relations.

### Create Truth Table from LaTeX Expression

> Obsidian command name: `Create truth table from LaTeX expression (markdown)` / `Create truth table from LaTeX expression (LaTeX)`

This command requires the input is a [proposition](MISSING_LINK).

[`sympy.logic.boolalg.truth_table`](https://docs.sympy.org/latest/modules/logic.html#sympy.logic.boolalg.truth_table) is used to generate a truth table of the proposition input, which is then inserted either as a LaTeX array, or a markdown table depending on the chosen command.

The input permutations are shown in the left most columns, and the proposition value is shown in the right most column.

### Convert LaTeX Expression To Sympy

This command parses the LaTeX input, and places the parsed sympy code into a `python` code block, below the input.

Definitions and assumptions are currently **NOT** included, and need to be added in manually.
