import sys
from readers.pptx_reader import read_pptx
from readers.pdf_reader import read_pdf
from processor.cleaner import clean_text
from processor.chunker import chunk_text
from summarizer.easy_summary import generate_easy_summary


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <pptx_or_pdf_file>")
        return

    file_path = sys.argv[1]

    if file_path.endswith(".pptx"):
        raw = read_pptx(file_path)
    elif file_path.endswith(".pdf"):
        raw = read_pdf(file_path)
    else:
        print("❌ Unsupported file format")
        return

    cleaned = clean_text(raw)
    chunks = chunk_text(cleaned, chunk_size=3)

    print(f"\n✔ Easy Summary Output\n")

    for idx, chunk in enumerate(chunks, start=1):
        print(f"📘 Chunk {idx} Summary:")
        summary = generate_easy_summary(chunk)
        print(summary)
        print("-" * 50)


if __name__ == "__main__":
    main()
