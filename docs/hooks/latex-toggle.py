import regex


def on_page_mardkwon(markdown: str, **_kwargs):
    pattern = r"$($\n)?(.*?)(\n$)?$"

    def replace_block(match):
        latex_source = match.group(1).strip()

        indented_latex = "\n".join("\t" + line if line else "" for line in f'')
