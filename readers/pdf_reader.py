# PDF reading logic
import pdfplumber


def read_pdf(file_path):
    pages_text = []

    with pdfplumber.open(file_path) as pdf:
        for idx, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()

            if text:
                pages_text.append(
                    f"Page {idx}:\n{text.strip()}"
                )

    return pages_text
