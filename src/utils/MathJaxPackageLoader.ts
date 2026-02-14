import { loadMathJax } from "obsidian";

declare global {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const MathJax: any;
}

// load the given set of latex packages via. injecting `\require` strings into MathJax.
export async function mathjaxLoadLatexPackages(latex_packages: string[]) {

    for (const latex_package of latex_packages) {
        mathjaxLoadLatexPreamble(`\\require{${latex_package}}`);
    }

}

export async function mathjaxLoadLatexPreamble(latex_preamble: string) {
    await loadMathJax();

    if (MathJax.tex2chtml == undefined) {
        MathJax.startup.ready = () => {
            MathJax.startup.defaultReady();
            MathJax.tex2chtml(latex_preamble);
        };
    } else {
        MathJax.tex2chtml(latex_preamble);
    }
}
