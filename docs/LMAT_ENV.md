<!-- omit in toc -->
# LaTeX Math Environments

**LaTeX Math** environments are used to configure CAS options for a section of a note.

The persistence of **LaTeX Math** environments are location based.

A new environment declaration resets all previous configurations to their default values, including variables defined through `$ .. := .. $`.

Environments are declared directly in the note with an `lmat` code block.

Below is a preview of the default **LaTeX Math** environment used, when no other environment has been declared.

<pre>
```lmat
<a href="##symbols">[symbols]</a>

[units]
<a href="##unit-system">system</a> = "SI"

[solve]
<a href="##default-solve-domain">domain</a> = "Complexes"
```
</pre>

<!-- omit in toc -->
## Table of Contents

- [Symbol Assumptions](#symbol-assumptions)
- [Unit System](#unit-system)
- [Default Solve Domain](#default-solve-domain)

## Symbol Assumptions

Assumptions are specified for a single symbol by assigning a list of [sympy assumptions](https://docs.sympy.org/latest/guides/assumptions.html#id28) to the symbol name, under the `symbols` table.

```toml
[symbols]
x = [ "real", "positive" ]
y = [ "integer", ... ]
...
```

A preview is also generated of the symbol assumptions, whilst the `lmat` code block is not being edited.

## Unit System

The default unit system to use when auto converting between units can be specified in the `system` field under the `units` table.

```toml
[units]
system = "..."
```

The value must be a string equal to one of the names in the **Unit System Name** column:

| Unit System Name | Base Units                                             |
| ---------------- | ------------------------------------------------------ |
| SI               | meter, kilogram, second, ampere, mole, candela, kelvin |
| MKSA             | meter, kilogram, second, ampere                        |
| MKS              | meter, kilogram, second                                |
| Natural system   | hbar, electronvolt, speed of light                     |

## Default Solve Domain

The default solution domain for single equations can be set in the `domain` field under the `solve` table.

```toml
[solve]
domain = "..."
```

This must be a string equal to the name of a [sympy fancy set](https://docs.sympy.org/latest/modules/sets.html#module-sympy.sets.fancysets) (e.g. "Reals" for the real numbers or "Naturals" for all natural numbers).
