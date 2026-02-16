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

> [!important] Exercise
> Translate the following natural language expressions into \(\LaTeX\) and evaluate them with **LaTeX Math**.
>
> a) one plus one.
>
> b) three over four.
>
> c) three over four, raised to the power of one plus one
>
> > [!success]- answers
> >
> > a) `1 + 1 = 2`
> >
> > b) `\frac{3}{4}`
> >
> > c) `\left( \frac{3}{4} \right)^{(1 + 1)} = \frac{9}{16}`
> >
> > Notice that most purely visual commands like `\left`, `\right`, `\quad`, .. are allowed and will simply be ignored by the parser.

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

Matrix types can be indexed by prepending them with an *index* operator, of the form `_{[r, c]}` or `_{[i]}`, where `r` and `c` is the <u>r</u>ow and <u>c</u>olumn to index, and `i` is the <u>i</u>ndex in a vector.
Note that matrices are **0 indexed**, meaning a value of 0 must be supplied, in order to index the first row / column of a matrix.

> [!important] Exercise
> Translate the following natural language expressions into \(\LaTeX\) and evaluate them with **LaTeX Math**.
>
> a) the matrix symbol \(M\) indexed at \(x, y\). (remember matrix symbols are commonly bold)
>
> b) The binary number `0011` multiplied with the octal number 16
>
> c) A [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix) with \(\theta = \frac{\pi}{2}\)
>
> > [!success]- answers
> >
> > a) `\mathbf{M}_{[x, y]}`
> >
> > b) `0b0011 \cdot 0o16 = 42`
> >
> > c) `\begin{bmatrix} \cos \frac{\pi}{2} & - \sin \frac{\pi}{2} \\ \sin \frac{\pi}{2} & \cos \frac{\pi}{2} \end{bmatrix} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}`
> >
> > Take note of how much we repeated ourselves in the solution to c)! This will be addressed in [AAA](MISSING-LINK).

## Built-in Functions

In addition to the arithmetic operators, various mathematical functions are also supported.
This subsection will provide a brief overview of the most commonly used ones, please go to the [reference](MISSING-LINK) for a full list.

Some basic functions include `\sqrt ..` ([square root](https://en.wikipedia.org/wiki/Square_root)) and `\exp ..` ([exponential function](https://en.wikipedia.org/wiki/Exponential_function)).

In addition to these, all the [trigonometric functions](https://en.wikipedia.org/wiki/Trigonometric_functions) are also supported (e.x. `\sin`, `\cos`, `\arccot`).
These functions expect their input to be in [radians](https://en.wikipedia.org/wiki/Radian).

Functions from other areas of mathematics like combinatorics (e.x. `\binom`), complex numbers (e.x. `\Re`, `\Im`, `\arg`) and calculus (e.x. `\grad(..)` for the [gradient](https://en.wikipedia.org/wiki/Gradient) of an expression) are also integrated into the plugin.

> [!important] Exercise
> Translate the following natural language expressions into \(\LaTeX\) and evaluate them with **LaTeX Math**.
>
> a) The sum of sine of \(x\) squared and cosine of \(x\) squared.
>
> b) \(e\) raised to the power of the product between the imaginary constant and pi.
>
> c) A north-east pointing \(2\)d unit vector, scaled by one fourth. 
>
> > [!success]- answers
> >
> > a) `\sin^2 x + \cos^2 x = 1`
> >
> > b) `e^{i \cdot \pi} = -1` or `\exp(i \cdot \pi)`
> >
> > c) `\begin{bmatrix} \frac{1}{\sqrt 2} \\ \frac{1}{\sqrt 2} \end{bmatrix}`

<!-- ## Putting It To Use

In this section, we will use our new tools to solve a problem, which is done trivially using **LaTeX Math**.

So let's get started.

Consider the following expression.
$$
x^2 + y^3 - 5 y
$$

At which $(x, y)$ pairs does this expression have [stationary points](https://en.wikipedia.org/wiki/Stationary_point)?

## Derivatives and Integrals
NOT CORRECT, just ordered by x, y, z, then u, v s and t or smnthng and then alphabetically.
To differentiate expressions with strictly 1 unknown variables, prepend them with primes (`'`).
Note that only this limited subset of the [Lagrange notation](https://en.wikipedia.org/wiki/Notation_for_differentiation) is supported.
> [!example]
> Below expression correctly computes the derivative of `x^2`
> 
> ```latex
> $$
> (x^2)' = 2x
> $$
> ```
> 
> But this expression fails, because there are 2 unknowns (`x` and `y`), so **LaTeX Math** does not know which one to pick.
> 
> ```latex
> $$
> (x + y)'
> $$
> ```

### Leibniz Notation

Leibniz notation should be used in place of [Lagrange notation](#lagrange-notation) when the expression contains multiple unknown variables, and thus requires computing a [partial derivative](https://en.wikipedia.org/wiki/Notation_for_differentiation#Partial_derivatives).
This notation can be written using a standard `\frac` command, and the special `\dd` differential operator command, or using the `\dv` command from the [physics package](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.5).

[!example]

```latex
$$
\frac{\dd \sin x \cdot \sin y}{\dd x \dd y} = \cos x \cos y
$$
```

```latex
$$
\dv{\dd \sin x \cdot \sin y}{\dd x \dd y} = \cos x \cos y
$$
``` -->