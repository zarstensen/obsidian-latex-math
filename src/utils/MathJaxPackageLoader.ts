import { loadMathJax } from "obsidian";

declare global {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const MathJax: any;
}

// load the given set of latex packages via. injecting `\require` strings into MathJax.
export async function mathjaxLoadLatexPackages(latex_packages: string[]) {
    await loadMathJax();
    
    for (const latex_package of latex_packages) {
        const require_str = `\\require{${latex_package}}`;

        if (MathJax.tex2chtml == undefined) {
            MathJax.startup.ready = () => {
                MathJax.startup.defaultReady();
                MathJax.tex2chtml(require_str);
            };
        } else {
            MathJax.tex2chtml(require_str);
        }
    }

}
