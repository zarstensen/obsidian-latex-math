---
title: 2.1 Evaluating Expressions
---

# Evaluating Expressions

You already learnt how to evaluate expressions in [1.2 First Evaluation](../1-Gettings-Started/2-first-evaluation.md) through the `LaTeX Math: Evaluate LaTeX expression` command.
Now you know the various ways of evaluating expressions with **LaTeX Math**, but you may still be wondering *what* exactly an expression can consist of. 

So, to start off, all [arithmetic operators](https://en.wikipedia.org/wiki/Arithmetic#Operations) can be used in expressions:

- `+`, `-` for addition and subtraction
- `\cdot` for multiplication
- `\frac{..}{..}` for division
- `^` for exponentiation
- `\log_{..}` for logarithm
- `(..)`, `[..]`, `{..}` for parenthetical subexpressions.

Other aliases for these operators, like `\dfrac{..}{..}` instead of `\frac{..}{..}` can also be used, these are detailed for each operator in the [reference](MISSING-LINK).

> [!example] Example Expression Using All Arithmetic Operators
> The below expressions showcases all the above operators in a singular expression.
> 
> ```latex
> (4^{\frac{1}{2}} + \log_{10} 100) \cdot (-2) = -8
> ```

## Values and Symbols

**LaTeX Math** supports both working with concrete numerical values or abstract undefined symbols.

**Numerical values** are denoted by just writing any integer or decimal number. Please note that **LaTeX Math** uses `.` as the [decimal separator](https://en.wikipedia.org/wiki/Decimal_separator), and there is currently no support for a thousands separator.
So $\frac{1}{2}$ is the same as `0.5` and `10,000` is not *currently* a valid numeric number.

Additionally, numbers can be written as binary, hex or octal numbers by prefixing them with `0b`, `0x` and `0o`.

> [!example]
> The below expression consists of a sum between a fraction, a decimal value, and a binary value.
>
> ```latex
> $$
> \frac{3}{5} + 0.4 - 0b1001 = -8.0
> $$
> ```

**Symbols** are denoted by writing a series of characters from the English alphabet.
Symbols may additionally be *indexed* with `_` (e.x. `x_{i}`) or *formatted* with commands like `\mathrm`[^format] (e.x. `\mathrm{v}`).
Note that symbols may consist of multiple characters, so `ab` is a distinct symbol from `a` and `b`.
This means that whilst `$ab$` and `$a b$` looks the same when rendered, they do not represent the same expression.

[^format]: see here for a full list of formatters [ref](MISSING-LINK)

The symbols `e`, `i` and `\pi` are predefined to be equal to [eulers number](https://en.wikipedia.org/wiki/E_(mathematical_constant)), the [imaginary unit](https://en.wikipedia.org/wiki/Imaginary_unit) and [pi](https://en.wikipedia.org/wiki/Pi).

**Matrices** are specified by placing values in any [matrix](https://www.overleaf.com/learn/latex/Matrices) or array environment.
As an example, the following matrix $\begin{bmatrix} 1 & 2 \\ a & bc \end{bmatrix}$ can be written as `$\begin{bmatrix} 1 & 2 \\ a & bc \end{bmatrix}$`.

## Built-in Functions

In addition to the arithmetic operators, various mathematical functions are also supported.
This subsection will provide a brief overview of the most commonly used ones, please go to the [reference](MISSING-LINK) for a full list.

Some basic functions include `\sqrt ..` ([square root](https://en.wikipedia.org/wiki/Square_root)) and `\exp ..` ([exponential function](https://en.wikipedia.org/wiki/Exponential_function)).

In addition to these, all the [trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions) are also supported (e.x. `\sin`, `\cos`, `\arccot`).
These functions expect their input to be in [radians](https://en.wikipedia.org/wiki/Radian).

Functions from other areas of mathematics like combinatorics (e.x. `\binom`), complex numbers (e.x. `\Re`, `\Im`, `\arg`) and linear algebra (e.x. `\mathbf{H}_{..}` for the [hessian matrix](https://en.wikipedia.org/wiki/Hessian_matrix)) can also be used.

## Derivatives and Integrals

TODO: write this...