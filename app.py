import streamlit as st
import os

from readers.pptx_reader import read_pptx
from readers.pdf_reader import read_pdf
from processor.cleaner import clean_text
from processor.chunker import chunk_text

from summarizer.easy_summary import generate_easy_summary
from summarizer.key_terms import extract_key_terms
from summarizer.questions import generate_questions

from utils.cache import get_file_hash, load_cache, save_cache


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Study Summarizer",
    page_icon="📘",
    layout="centered"
)

st.title("📘 Study Summarizer")
st.write("Upload your **PPTX or PDF** and get a **5-minute student-friendly summary**.")


# ---------------- UI CONTROLS ----------------
uploaded_file = st.file_uploader(
    "📂 Upload PPTX or PDF file",
    type=["pptx", "pdf"]
)

summary_mode = st.radio(
    "📄 Summary Mode",
    ["Preview (First Part)", "Full Summary"]
)

exam_mode = st.checkbox("🎯 Exam Focused Summary")
language = st.selectbox("🌍 Summary Language", ["English", "Bangla"])


# ---------------- MAIN LOGIC ----------------
if uploaded_file:

    file_name = uploaded_file.name
    file_ext = file_name.split(".")[-1]

    file_bytes = uploaded_file.getvalue()
    file_hash = get_file_hash(file_bytes)

    # cache key must include all user options
    cache_key = f"{file_hash}_{summary_mode}_{language}_{exam_mode}"

    temp_path = f"temp.{file_ext}"
    with open(temp_path, "wb") as f:
        f.write(file_bytes)

    st.success("File uploaded successfully ✅")

    cache = load_cache()

    if st.button("✨ Generate Summary"):

        with st.spinner("Analyzing and summarizing..."):

            # ---------- CACHE CHECK ----------
            if cache_key in cache:
                final_summary = cache[cache_key]
                st.info("⚡ Loaded from cache (API not used)")
                first_chunk = None

            else:
                # ---------- READ FILE ----------
                if file_ext == "pptx":
                    raw = read_pptx(temp_path)
                else:
                    raw = read_pdf(temp_path)

                # ---------- PIPELINE ----------
                cleaned = clean_text(raw)
                chunks = chunk_text(cleaned, chunk_size=3)

                if summary_mode == "Preview (First Part)":
                    chunks_to_process = chunks[:1]
                else:
                    chunks_to_process = chunks

                final_summary = ""

                for i, chunk in enumerate(chunks_to_process, start=1):
                    summary = generate_easy_summary(
                        chunk_text=chunk,
                        exam_mode=exam_mode,
                        language=language
                    )
                    final_summary += f"Part {i} Summary:\n{summary}\n\n"

                first_chunk = chunks[0]

                # ---------- SAVE CACHE ----------
                cache[cache_key] = final_summary
                save_cache(cache)

        # ---------------- OUTPUT ----------------
        st.subheader("📄 Summary Output")
        st.text(final_summary)

        st.download_button(
            label="⬇️ Download Summary (.txt)",
            data=final_summary,
            file_name=f"{file_name}_summary.txt",
            mime="text/plain"
        )

        # ---------------- EXTRA FEATURES ----------------
        if first_chunk:
            st.subheader("📌 Important Key Terms")
            key_terms = extract_key_terms(first_chunk)
            st.text(key_terms)

            if st.button("✍️ Generate Possible Exam Questions"):
                questions = generate_questions(first_chunk, language)
                st.subheader("✍️ Possible Exam Questions")
                st.text(questions)

        st.success("Done! Ready to study 📚")

    # ---------------- CLEANUP ----------------
    if os.path.exists(temp_path):
        os.remove(temp_path)
