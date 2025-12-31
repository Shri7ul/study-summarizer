import os

STRUCTURE = {
    "main.py": "",
    "app.py": "",
    ".env": "#GEMINI_API_KEY=your_api_key_here",
    "requirements.txt": "",
    "README.md": "",
    "outputs": {},
    "readers": {
        "__init__.py": "",
        "pptx_reader.py": "# PPTX reading logic\n",
        "pdf_reader.py": "# PDF reading logic\n",
    },
    "processor": {
        "__init__.py": "",
        "cleaner.py": "# text cleaning logic\n",
        "chunker.py": "# text chunking logic\n",
    },
    "summarizer": {
        "__init__.py": "",
        "easy_summary.py": "# easy & short summary logic\n",
        "key_terms.py": "",
        "questions.py": "",
    },
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)

        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == "__main__":
    create_structure(".", STRUCTURE)
    print("✅study-summarizer structure ready (existing files untouched)")
