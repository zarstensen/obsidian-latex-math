declare global {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const MathJax: any;
}

export function mathjaxLoadLatexPackages(latex_packages: string[]) {
    for (const latex_package in latex_packages) {
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
