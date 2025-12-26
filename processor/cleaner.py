# text cleaning logic
import re


def clean_text(blocks):
    """
    blocks: list[str]  (slides/pages text)
    returns: list[str] (cleaned text blocks)
    """

    cleaned_blocks = []

    for block in blocks:
        lines = block.splitlines()
        clean_lines = []

        for line in lines:
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            # skip page/slide numbers only
            if line.isdigit():
                continue

            # skip very short junk lines
            if len(line) < 3:
                continue

            # normalize spaces
            line = re.sub(r"\s+", " ", line)

            clean_lines.append(line)

        if clean_lines:
            cleaned_blocks.append("\n".join(clean_lines))

    return cleaned_blocks
