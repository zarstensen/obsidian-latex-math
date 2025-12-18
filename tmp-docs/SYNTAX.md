<!-- omit in toc -->
# LaTeX Math Syntax

This document aims to provide an overview of the LaTeX parsing capabilities of this plugin. As a general note, the parser was designed with standard LaTeX notation in mind, so as long as you avoid complex formatting or esoteric math functions, it should be straightforward to write LaTeX formulas that the plugin can parse.

While this document provides a good overview of the parser, you can also consult the [grammar files](lmat-cas-client/lmat_cas_client/grammar/latex_math_grammar.lark) for the concrete implementation.

<!-- omit in toc -->
## Table of Contents

- [Extra LaTeX Packages](#extra-latex-packages)
- [Expression Structure](#expression-structure)
  - [Expression](#expression)
  - [Logical Proposition](#logical-proposition)
- [Ignored Tokens](#ignored-tokens)
- [Numbers](#numbers)
- [Symbols](#symbols)
- [Matrices](#matrices)
  - [Delimiters in Matrix Environments](#delimiters-in-matrix-environments)
- [Mathematical Functions and Operations](#mathematical-functions-and-operations)
- [Mathematical Constants](#mathematical-constants)
- [Logical Operators](#logical-operators)
- [Units and Physical Constants](#units-and-physical-constants)
  - [Supported Units](#supported-units)
  - [Supported Physical Constants](#supported-physical-constants)

## Extra LaTeX Packages

**LaTeX Math** includes the following LaTeX, to provide a smoother user experience, and avoid some potential ambiguity issues in the latex parser.

Note that only a subset of the syntax the packages provide is supported by the **LaTeX Math** parser. This is highlighted as a bullet point list below each package.

[**physics**](https://ctan.org/pkg/physics?lang=en):

- [`\vectorbold` and `\vectorarrow`](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.2) as symbol formatters.
- [`\vectorunit`](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.2) for computing the unit vector of a supplied vector.
- [`\dotproduct`](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.2) as an alternative multiplication operator.
- [`\crossproduct`](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.2) for computing the cross product of 2 3d vectors.
- [`\gradient`](https://mirrors.dotsrc.org/ctan/macros/latex/contrib/physics/physics.pdf#subsection.2.2) as an alternative to `\nabla`.
- [`\trace`](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf#subsection.2.3) for computing the trace of a matrix.
- [`\differential`](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf#subsection.2.5) to denote differential symbol `d` in derivatives and integrals.
- [`\derivative` and `\partialderivative`](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf#subsection.2.5) for shorthand versions of partial derivatives.

## Expression Structure

The **LaTeX Math** parser is able to parse most [mathematical expressions and relations](#expression) (*e.g.* `>`, `<`, `=`) between expressions, as well as [logical propositions](#logical-proposition).

### Expression

An expression is any series of mathematical terms separated by `+` or `-` signs.
Terms consists of a series of factors separated by a multiplication sign (`*`, `\cdot`, `\times`) or a division sign (`/`), where a factor is one of the following:

<!-- no toc -->
- [Number](#numbers)
- [Symbol](#symbols)
- [Unit / Constant](#units-and-physical-constants)
- [Matrix](#matrices)
- Exponentiation
- [Function](#mathematical-functions)
- Expression delimited by `()`, `{}` or `[]`

If no multiplication or division sign is present, multiplication is implicitly assumed.

The parser also supports systems of equations. Notate these by placing a series of equations, separated by latex newlines (`\\\\`), inside a `cases` or `align` environment.

### Logical Proposition

A logical proposition is any [logical operator](#logical-operators) applied on a [boolean constant](#mathematical-constants), [symbol](#symbols), [expression](#expression), [relation](#expression) or another logical proposition.

Logical propositions may be chained together with a `\equiv` symbol separating each proposition.

*e.g. `A \implies B \equiv B \vee \neg A`*

Expressions and logical propositions cannot be mixed. The only exception to this is the `iff` operator, which checks for symbolic equality if one of its arguments is an expression.

*e.g. `x^2 \implies 2 y`, `(x \wedge y) + 2` is NOT allowed, but `x \iff \sqrt{x^2}` is allowed, and checks if `x` is symbolically equal to `\sqrt{x^2}` upon evaluation*

## Ignored Tokens

Alignment tokens (`&` and `\\`), as well as any text command (`\text{...}`, `\textbf{...}`, `\textcolor{...}{...}`, ...), can be placed between other tokens anywhere in a latex string.

The parser will simply ignore these tokens and act as if they are not present.

## Numbers

Numbers can be notated in 1 of the following 4 ways.

- No prefix for base 10 e.g. `1234`.
- `0x` or `0X` prefix for hexadecimal (base 16) e.g. `0xFF12`.
- `0o` prefix for octal (base 8) e.g. `0o57`.
- `0b` prefix for binary (base 2) e.g. `0b10110100`.

Any prefixed number may optionally be surrounded with `\mathrm{...}`.
Only surrounding the character in the prefix is also allowed `0\mathrm{x|b|o}...`.

## Symbols

The parser understands various ways of notating symbols. The below table gives some examples for supported notation concepts.

| Type      | LaTeX String                                                       |
| :-------- | :----------------------------------------------------------------- |
| greek     | `\alpha` / `\beta` / `\gamma` / ...                                |
| latin     | `a` / `x` / `symbol` / ...                                         |
| formatted | `\mathrm{x}` / `\pmb{vector}` / `\mathit{whitespace symbol}` / ... |
| indexed   | `x_y` / `\alpha_\gamma` / `\pmb{M}_{1;2}` / ...                    |

> [!CAUTION]
> Note that Latin symbols spelling out Greek letters will be converted to Greek symbols upon evaluation e.g. the Latin symbol `alpha` will be output as `\alpha` upon evaluation.
> This is a side effect of how Sympy handles symbols internally.

## Matrices

A matrix can be notated via. the `matrix` environment, (or any other environment matching the regex `([bp]?(?:small)?)matrix`), or the `array` environment.

Transpositions of matrices are performed by inserting `^T` after a matrix value.

> [!NOTE]
> **Examples**
>
> 2 x 2 matrix with elements 1, 2, 3 and 4.
>
> ```latex
> \begin{bmatrix}
> 1 & 2 \\
> 3 & 4
> \end{bmatrix}
> ```
>
> 3d vector using the `array` environment
>
> ```latex
> \left[\begin{array}
> x \\
> y \\
> z
> \end{array}\right]
> ```

### Delimiters in Matrix Environments

Delimiters before and after `array` environments, and the type of `matrix` environment, are persisted through parsing and will be present in command outputs.

In case multiple matrices are computed into a single matrix, the left most matrix delimiters in the original expression is persisted in the output.

> [!NOTE]
> **Example**
>
> The output is a `bmatrix` as this was the left most matrix in the original expression.
>
> ```latex
> \begin{bmatrix} ... \end{bmatrix} + \begin{pmatrix} ... \end{pmatrix} = \begin{bmatrix} ... \end{bmatrix}
> ```

## Mathematical Functions and Operations

Below is a table of all supported mathematical functions and operations supported by the parser, this list may grow overtime as this project develops.
Note that a *mathematical function* also encompasses concepts not normally thought of as a function, e.g. `\frac` is considered part of this table whilst it may not intuitively be thought of as a function.

| Function                                                                                                                       | LaTeX String                                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| sine                                                                                                                           | `\sin`                                                                                       |
| cosine                                                                                                                         | `\cos`                                                                                       |
| tangent                                                                                                                        | `\tan`                                                                                       |
| secant                                                                                                                         | `\sec`                                                                                       |
| cosecant                                                                                                                       | `\csc`                                                                                       |
| cotangent                                                                                                                      | `\cot`                                                                                       |
| arcus sine                                                                                                                     | `\arcsin`                                                                                    |
| arcus cosine                                                                                                                   | `\arccos`                                                                                    |
| arcus tan                                                                                                                      | `\arctan`                                                                                    |
| arcus secant                                                                                                                   | `\arcsec`                                                                                    |
| arcus cosecant                                                                                                                 | `\arccsc`                                                                                    |
| arcus cotangent                                                                                                                | `\arccot`                                                                                    |
| hyperbolic sine                                                                                                                | `\sinh`                                                                                      |
| hyperbolic cosine                                                                                                              | `\cosh`                                                                                      |
| hyperbolic tangent                                                                                                             | `\tanh`                                                                                      |
| hyperbolic secant                                                                                                              | `\sech`                                                                                      |
| hyperbolic cosecant                                                                                                            | `\csch`                                                                                      |
| hyperbolic cotangent                                                                                                           | `\coth`                                                                                      |
| hyperbolic arcus sine                                                                                                          | `\mathrm{arsinh}` / `\operatorname{arsinh}`                                                  |
| hyperbolic arcus cosine                                                                                                        | `\mathrm{arcosh}` / `\operatorname{arcosh}`                                                  |
| hyperbolic arcus tangent                                                                                                       | `\mathrm{artanh}` / `\operatorname{artanh}`                                                  |
| hyperbolic arcus secant                                                                                                        | `\mathrm{arsech}` / `\operatorname{arsech}`                                                  |
| hyperbolic arcus cosecant                                                                                                      | `\mathrm{arcsch}` / `\operatorname{arcsch}`                                                  |
| hyperbolic arcus cotangent                                                                                                     | `\mathrm{arcoth}` / `\operatorname{arcoth}`                                                  |
| log                                                                                                                            | `\log[base]?` / `\ln` / `\lg`                                                                |
| real part                                                                                                                      | `\Re .` / `\mathrm{Re} .`                                                                    |
| imaginary part                                                                                                                 | `\Im .` / `\mathrm{Im} .`                                                                    |
| argument                                                                                                                       | `\arg .`                                                                                     |
| sign                                                                                                                           | `\mathrm{sgn} .` / `\operatorname{sgn} .`                                                    |
| exponential                                                                                                                    | `\exp .`                                                                                     |
| factorial                                                                                                                      | `. !`                                                                                        |
| percent                                                                                                                        | `. \%`                                                                                       |
| permille                                                                                                                       | `. \textperthousand`                                                                         |
| limit                                                                                                                          | `\lim_{ . \to . }`                                                                           |
| sum                                                                                                                            | `\sum_{ . = . }^.`                                                                           |
| product                                                                                                                        | `\prod_{ . = . }^.`                                                                          |
| minimum                                                                                                                        | `\min(. , . , ..., . )`                                                                      |
| maximum                                                                                                                        | `\max( . , . , ..., . )`                                                                     |
| standard inner product                                                                                                         | `\langle . \| . \rangle`                                                                     |
| vector cross product                                                                                                           | ` . \times . `                                                                               |
| numeric value                                                                                                                  | `\| . \|`                                                                                    |
| norm of matrix                                                                                                                 | `\Vert . \Vert` / `\|\| . \|\|`                                                              |
| unit vector from vector                                                                                                        | `\vectorunit .` / `\vu .`                                                                    |
| floor                                                                                                                          | `\lfloor . \rfloor`                                                                          |
| ceiling                                                                                                                        | `\lceil . \rceil`                                                                            |
| root                                                                                                                           | `\sqrt[index]?`                                                                              |
| conjugate                                                                                                                      | `\bar` / `\overline`                                                                         |
| fraction                                                                                                                       | `\frac{ . }{ . }`                                                                            |
| binomial                                                                                                                       | `\binom{ . }{ . }`                                                                           |
| partial derivative                                                                                                             | `\frac{ \dd ... }{ \dd . \dd . ... }` / `\frac{ \partial }{ \partial . \partial . ... } ...` |
| partial derivative [physics package](https://mirrors.ibiblio.org/CTAN/macros/latex/contrib/physics/physics.pdf#subsection.2.5) | `\dv[-order-]{-symbol-} -expression-` / `\dv[-order-]{-expression-}{-symbol-} ...`           |
| prime derivative                                                                                                               | `(...)'''...`                                                                                |
| integral                                                                                                                       | `\int ... \dd .` / `\int_a^b ... \dd .`                                                      |
| determinant                                                                                                                    | `\det .` / `\begin{vmatrix} ... \end{vmatrix}`                                               |
| trace                                                                                                                          | `\mathrm{trace} .` / `\operatorname{trace} .`                                                |
| adjugate                                                                                                                       | `\mathrm{adjugate} .` / `\operatorname{adjugate} .`                                          |
| reduced row echelon form                                                                                                       | `\mathrm{rref} .` / `\operatorname{rref} .`                                                  |
| gradient                                                                                                                       | `\nabla ...` / `\grad ...`                                                                   |
| hessian                                                                                                                        | `\mathbf{H} ...`                                                                             |
| Jacobian                                                                                                                       | `\mathbf{J} ...`                                                                             |
| permutations                                                                                                                   | `P( ... ,  ... )`                                                                            |
| combinations                                                                                                                   | `C( ... ,  ... )`                                                                            |
| derangements                                                                                                                   | `D( ... )` / `{ ! ... }`                                                                     |
| greatest common divisor                                                                                                        | `\gcd( ... ,  ... )`                                                                         |
| least common multiple                                                                                                          | `\mathrm{lcm}( ... ,  ... )` / `\operatorname{lcm}( ... ,  ... )`                            |
| modulo                                                                                                                         | `. \mod .`                                                                                   |
| Taylor polynomial                                                                                                              | `T_{-degree-, -index-, -expansion point (0 by default)-}(...)`                               |

## Mathematical Constants

Below is a table of all the mathematical constants the parser supports.

| Name                          | LaTeX String                                |
| :---------------------------- | :------------------------------------------ |
| pi                            | `\pi`                                       |
| euler                         | `e`                                         |
| imaginary unit                | `i`                                         |
| infinity                      | `\infty`                                    |
| boolean true[^boolean-const]  | `\mathrm{T}` / `\operatorname{True}` / ...  |
| boolean false[^boolean-const] | `\mathrm{F}` / `\operatorname{False}` / ... |

[^boolean-const]: These constants only apply inside logical propositions, they can be used as standard symbols in expressions, provided they are not the first token in said expression. e.g. `2 \mathrm{T}` is a valid expression, whilst `\mathrm{T} 2` is not, as `\mathrm{T}` is seen as the boolean true constant in this case.

## Logical Operators

Below is a list of logical operators this parser supports.
The order of precedence starts with any logical proposition surrounded by delimiters, and then follows the operators' entry in the below table, from top to bottom.
e.g. `\neg` has higher precedence than `\wedge` because it is higher in the list.

| Operator    | LaTeX String                                                         |
| :---------- | :------------------------------------------------------------------- |
| not         | `\neg .`                                                             |
| xnor        | `. \odot .`                                                          |
| xor         | `. \oplus .`                                                         |
| nor         | `. \bar \vee .` / `. \overline \vee .`                               |
| and         | `. \wedge .`                                                         |
| nand        | `. \bar \wedge .` / `. \overline \wedge .`                           |
| or          | `. \vee .`                                                           |
| implication | `. \implies .` / `. \leftarrow . ` / `. \Rightarrow .` / ...         |
| iff         | `. \iff .` / `. \leftrightarrow . ` / `. \rightleftharpoons .` / ... |

## Units and Physical Constants

Units and physical constants are specified by surrounding them with braces `{}`. This, in general, is prioritized lower than braces being used as parentheses, or as argument delimiters to functions. This means that `\sin{km}` for example is parsed as sine to the symbol *km*, and not the unit *kilometer*. To get the unit, it would have to be written like the following `\sin{{km}}`.

The only case where this is not true, is for the base factor in exponentiations. For example here `{km}^2` is seen as kilometers squared.

The following sections provide an overview of all the supported units of the parser.

Note: braces (`{}`) and underscores (`_`) are ignored when matching aliases, so as an example `{ full_{moon}_{cycles} }` would match the `fullmooncycles` unit alias.
This behavior is currently a workaround for some units and constants not being usable otherwise, but this is a temporary fix and will be removed in a future version of **LaTeX Math**,
so make sure to stay as close to the original aliases as possible to avoid future complications.

### Supported Units

| Unit                     | Aliases                           |
| :----------------------- | :-------------------------------- |
| ampere                   | amperes<br/>A                     |
| angstrom                 | angstroms                         |
| angular_mil              | mil<br/>angular_mils              |
| anomalistic_year         | anomalistic_years                 |
| astronomical_unit        | astronomical_units<br/>AU<br/>au  |
| atmosphere               | atmospheres<br/>atm               |
| bar                      | bars                              |
| becquerel                | Bq                                |
| bit                      | bits                              |
| byte                     | bytes                             |
| candela                  | cd<br/>candelas                   |
| centiliter               | cL<br/>cl<br/>centiliters         |
| common_year              | common_years                      |
| coulomb                  | C<br/>coulombs                    |
| curie                    | Ci                                |
| day                      | days                              |
| debye                    |                                   |
| deciliter                | dl<br/>deciliters<br/>dL          |
| degree                   | deg<br/>degrees                   |
| dioptre                  | optical_power<br/>D<br/>diopter   |
| draconic_year            | draconic_years                    |
| dyne                     |                                   |
| electron_rest_mass       | me                                |
| erg                      |                                   |
| farad                    | farads<br/>F                      |
| foot                     | ft<br/>feet                       |
| full_moon_cycle          | full_moon_cycles                  |
| gauss                    |                                   |
| gaussian_year            | gaussian_years                    |
| gram                     | g<br/>grams                       |
| gray                     | Gy                                |
| hectare                  | ha                                |
| henry                    | H<br/>henrys                      |
| hertz                    | Hz<br/>hz                         |
| hour                     | hours<br/>h                       |
| inch                     | inches                            |
| joule                    | J<br/>joules                      |
| julian_year              | julian_years                      |
| katal                    | kat                               |
| kelvin                   | kelvins<br/>K                     |
| lightyear                | lightyears<br/>ly                 |
| liter                    | liters<br/>l<br/>L                |
| lux                      | lx                                |
| maxwell                  |                                   |
| meter                    | meters<br/>m                      |
| mile                     | mi<br/>miles                      |
| milli_mass_unit          | mmu<br/>mmus                      |
| milliliter               | milliliters<br/>ml<br/>mL         |
| minute                   | minutes<br/>min                   |
| mmHg                     | torr                              |
| mole                     | mol<br/>moles                     |
| nautical_mile            | nmi<br/>nautical_miles            |
| newton                   | N<br/>newtons                     |
| oersted                  |                                   |
| ohm                      | ohms                              |
| pascal                   | Pa<br/>pascals<br/>pa             |
| percent                  | percents                          |
| permille                 |                                   |
| planck_acceleration      | a_P                               |
| planck_angular_frequency | omega_P                           |
| planck_area              |                                   |
| planck_charge            | q_P                               |
| planck_current           | I_P                               |
| planck_density           | rho_P                             |
| planck_energy            | E_P                               |
| planck_energy_density    | rho^E_P                           |
| planck_force             | F_P                               |
| planck_impedance         | Z_P                               |
| planck_intensity         |                                   |
| planck_length            | l_P                               |
| planck_mass              | m_P                               |
| planck_momentum          |                                   |
| planck_power             | P_P                               |
| planck_pressure          | p_P                               |
| planck_temperature       | T_P                               |
| planck_time              | t_P                               |
| planck_voltage           | V_P                               |
| planck_volume            |                                   |
| pound                    | pounds                            |
| psi                      |                                   |
| quart                    | quarts                            |
| radian                   | rad<br/>radians                   |
| rutherford               | Rd                                |
| second                   | s<br/>seconds                     |
| sidereal_year            | sidereal_years                    |
| siemens                  | mho<br/>mhos<br/>S                |
| statampere               |                                   |
| statcoulomb              | statC<br/>franklin                |
| statvolt                 |                                   |
| steradian                | sr<br/>steradians                 |
| tesla                    | T<br/>teslas                      |
| tropical_year            | year<br/>years<br/>tropical_years |
| volt                     | volts<br/>v<br/>V                 |
| watt                     | W<br/>watts                       |
| weber                    | Wb<br/>wb<br/>webers              |
| yard                     | yd<br/>yards                      |

### Supported Physical Constants

| Constant                    | Aliases                                                  |
| :-------------------------- | :------------------------------------------------------- |
| acceleration_due_to_gravity | gee<br/>gees                                             |
| atomic_mass_constant        | amu<br/>Da<br/>dalton<br/>atomic_mass_unit<br/>amus      |
| avogadro_constant           | N_A<br/>avogadro                                         |
| avogadro_number             | N_0                                                      |
| boltzmann_constant          | boltzmann                                                |
| coulomb_constant            | electric_force_constant<br/>coulombs_constant<br/>k_e    |
| electron_mass               | m_e                                                      |
| electronvolt                | eV                                                       |
| elementary_charge           | e                                                        |
| faraday_constant            |                                                          |
| gravitational_constant      | G                                                        |
| hbar                        |                                                          |
| josephson_constant          | K_j                                                      |
| magnetic_constant           | \mu_0<br/>vacuum_permeability<br/>mu_0<br/>u_0           |
| molar_gas_constant          | R                                                        |
| neutron_mass                | m_n                                                      |
| planck                      |                                                          |
| proton_mass                 | m_p                                                      |
| speed_of_light              | c                                                        |
| stefan_boltzmann_constant   | stefan                                                   |
| vacuum_impedance            | Z_0                                                      |
| electric_constant           | \epsilon_0<br/>vacuum_permittivity<br/>e_0<br/>epsilon_0 |
| von_klitzing_constant       | R_k                                                      |
