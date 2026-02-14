---
title: 1.2 First Evaluation
---

# First Evaluation

Now that you have installed the plugin, it is time to actually use it!

The most basic thing you can do with this plugin, is to evaluate a [mathematical expression](https://en.wikipedia.org/wiki/Expression_(mathematics)) in a LaTeX math block (text surrounded with `$..$` or `$$..$$`).
To perform your first evaluation, create a math block containing a simple expression.
An example could be something like the following:

```latex
$$
1 + 1
$$
```

Place your cursor somewhere inside this math block, press ++ctrl+p++ to open up the *Command Palette*, and search + execute a command called `LaTeX Math: Evaluate LaTeX expression`.

>[!note]
>If you have just installed / updated your plugin, it may take a couple of minutes before the result is inserted, as it takes a while to extract the cas client and compile the grammar file.
>However, the compile result is cached, so it should only take a couple of seconds to load whenever you open up Obsidian again.

**LaTeX Math** should now append the result to your expression:

```latex
$$
1 + 1 = 2
$$
```

And that is it! Now you know how to use the core functionality of the plugin.
It is highly recommended you create a hotkey for the `LaTeX Math: Evaluate LaTeX expression`, as this is the command you likely are going to use the most.


With this, you are set to use the most common use case for this plugin.
However, there is still much to explore, just continue with this tutorial to learn how to solve equations, define variables and assumptions on symbols, work with units, and more...
