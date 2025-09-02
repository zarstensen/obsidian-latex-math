
<!-- omit in toc -->
# LaTeX Math Commands

This document provides detailed descriptions for all obsidian commands provided by the **LaTeX Math** plugin. For a quick overview, take a look at the [README command list](../README.md#command-list).

## General Information

In general, all commands require a LaTeX expression as input. Below is the list of methods for determining what this input should consist of, ordered by decreasing priority.

- **Selection is present:** Use selection as the input.
- **Cursor is inside a math block:**[^math-block] Use the contents of the math block as input.
- **Otherwise:** Input cannot be determined, show an error to the user.

[^math-block]: A math block is any text surrounded by unescaped dollar signs '$'.

If a command is being processed for longer than some set time (currently 1 sec), **LaTeX Math** will display a clickable 'evaluating' entry in the Obsidian status bar.

Upon clicking this, one gets the option to interrupt all currently processed commands.

This is especially useful if you accidentally try to evaluate an intensive expression, which may never finish within a reasonable time frame.

<!-- omit in toc -->
## Table Of Contents

- [General Information](#general-information)
- [Evaluate LaTeX Expression](#evaluate-latex-expression)
- [Evalf LaTeX Expression](#evalf-latex-expression)
- [Factor LaTeX Expression](#factor-latex-expression)
- [Expand LaTeX Expression](#expand-latex-expression)
- [Partial Fraction Decompose LaTeX Expression](#partial-fraction-decompose-latex-expression)
- [Convert Units In LaTeX Expression](#convert-units-in-latex-expression)
- [Solve LaTeX Expression](#solve-latex-expression)
- [Create Truth Table from LaTeX Expression](#create-truth-table-from-latex-expression)
- [Convert LaTeX Expression To Sympy](#convert-latex-expression-to-sympy)

## Evaluate LaTeX Expression

## Evalf LaTeX Expression

## Factor LaTeX Expression

## Expand LaTeX Expression

## Partial Fraction Decompose LaTeX Expression

## Convert Units In LaTeX Expression

## Solve LaTeX Expression

## Create Truth Table from LaTeX Expression

## Convert LaTeX Expression To Sympy
