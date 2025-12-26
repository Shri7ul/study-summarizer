import streamlit as st
import os
from readers.pptx_reader import read_pptx
from readers.pdf_reader import read_pdf
from processor.cleaner import clean_text
from processor.chunker import chunk_text
from summarizer.easy_summary import generate_easy_summary


st.set_page_config(
    page_title="Study Summarizer",
    page_icon="📘",
    layout="centered"
)

st.title("📘 Study Summarizer")
st.write("Upload your **PPTX or PDF** and get a **5-minute easy summary**.")

uploaded_file = st.file_uploader(
    "Upload PPTX or PDF file",
    type=["pptx", "pdf"]
)

if uploaded_file:
    file_name = uploaded_file.name
    file_ext = file_name.split(".")[-1]

    temp_path = f"temp.{file_ext}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    if st.button("✨ Generate Summary"):
        with st.spinner("Analyzing and summarizing..."):
            # Read file
            if file_ext == "pptx":
                raw = read_pptx(temp_path)
            else:
                raw = read_pdf(temp_path)

            # Process pipeline
            cleaned = clean_text(raw)
            chunks = chunk_text(cleaned, chunk_size=3)

            final_summary = ""

            for i, chunk in enumerate(chunks, start=1):
                summary = generate_easy_summary(chunk)
                final_summary += f"📘 Part {i} Summary:\n{summary}\n\n"

            # Save output
            os.makedirs("outputs", exist_ok=True)
            output_path = f"outputs/{file_name}_summary.txt"

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(final_summary)

        st.subheader("📄 Summary Output")
        st.text(final_summary)

        st.download_button(
            label="⬇️ Download Summary (.txt)",
            data=final_summary,
            file_name=f"{file_name}_summary.txt",
            mime="text/plain"
        )

        st.success("Summary ready!")

    # Cleanup
    os.remove(temp_path)
