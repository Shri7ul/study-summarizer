# 🧠 Project Blueprint — Study Summarizer

This document describes the **architecture, logic flow, and design decisions** behind the **Study Summarizer** project.

The goal of this blueprint is to make the project:
- Easy to understand
- Easy to extend
- Easy to debug or maintain

---

## 🎯 Project Goal

Students often receive large **PPTX or PDF lecture materials** that take a lot of time to read.

**Study Summarizer** solves this by converting:
> 20–30 minutes of lecture content → **5-minute easy, exam-focused summaries**

The project is designed for **real student usage**, not just demo purposes.

---

## 🧩 High-Level Architecture
```yaml 
User (Browser)
↓
Streamlit UI (app.py)
↓
Input Reader (PPTX / PDF)
↓
Text Cleaning
↓
Chunking (AI-safe size)
↓
AI Processing (Gemini)
↓
Post Processing
↓
Output + Cache

```

---

## 📁 Folder Structure Overview
```bash
study-summarizer/
│
├── app.py # Streamlit UI (entry point)
├── main.py # CLI runner (optional)
│
├── readers/ # Input readers
│ ├── pptx_reader.py
│ └── pdf_reader.py
│
├── processor/ # Text processing logic
│ ├── cleaner.py
│ └── chunker.py
│
├── summarizer/ # AI logic
│ ├── easy_summary.py
│ ├── key_terms.py
│ └── questions.py
│
├── utils/ # Utilities
│ └── cache.py
│
├── outputs/ # Generated files & cache
│ └── cache.json
│
├── .env # API key (not committed)
├── requirements.txt
├── README.md
└── blueprint.md # This file

```

---

## 🔄 Detailed Pipeline Flow

### 1️⃣ File Upload (UI Layer)
- User uploads a **PPTX or PDF**
- File bytes are captured
- A temporary file is created for processing

Handled in:
- `app.py`

---

### 2️⃣ Cache Key Generation
To avoid unnecessary API calls, a **smart cache key** is created using:

file_hash + summary_mode + language + exam_mode

yaml
Copy code

This ensures:
- Same file + same options → cache hit
- Any option change → fresh summary

Handled in:
- `utils/cache.py`

---

### 3️⃣ Input Reading
Depending on file type:
- PPTX → slide-wise text extraction
- PDF → page-wise text extraction

Handled in:
- `readers/pptx_reader.py`
- `readers/pdf_reader.py`

Output:
- List of raw text blocks

---

### 4️⃣ Text Cleaning
Raw extracted text may contain:
- Empty lines
- Page numbers
- Extra spaces

Cleaning rules:
- Remove empty/junk lines
- Normalize spacing
- Keep meaningful content only

Handled in:
- `processor/cleaner.py`

---

### 5️⃣ Chunking (AI Safety Layer)
AI models cannot reliably process very large text at once.

Chunking rules:
- Default: **3 slides/pages per chunk**
- Maintains logical flow
- Prevents API overload

Handled in:
- `processor/chunker.py`

---

### 6️⃣ Summary Mode Logic
Two modes are supported:

- **Preview Mode**
  - Only first chunk is summarized
  - Saves API usage

- **Full Summary Mode**
  - All chunks are summarized

Controlled in:
- `app.py`

---

### 7️⃣ AI Summarization (Core Intelligence)

Powered by **Gemini 2.5 Flash**

Features:
- Exam-focused summaries
- Bangla / English support
- Plain text output (no markdown)
- Student-friendly tone

Handled in:
- `summarizer/easy_summary.py`

---

### 8️⃣ Additional AI Features

#### 📌 Key Terms Extraction
Extracts important technical terms for revision.

Handled in:
- `summarizer/key_terms.py`

---

#### ✍️ Question Generation
Generates possible **2–5 marks exam questions**.

Handled in:
- `summarizer/questions.py`

---

### 9️⃣ Output & Download
- Summary is shown in UI
- User can download `.txt` file
- Cache is updated for future reuse

Handled in:
- `app.py`
- `outputs/`

---

## ⚡ Cache System Design

Cache behavior:
- Stored as `outputs/cache.json`
- Automatically handles:
  - Missing file
  - Empty file
  - Corrupted JSON

Benefits:
- Reduces API usage
- Faster response
- Production-grade reliability

---

## 🔒 Security & Ethics

- API key stored in `.env`
- `.env` excluded from version control
- No personal data stored
- Designed strictly for **educational purposes**

---

## 🚀 Extensibility (Future Ideas)

The architecture allows easy extension:
- Handwritten-style notes
- PDF export
- Audio lecture support
- SaaS authentication layer
- Paid / quota-based full summary

---

## 👤 Author

**InHuman**

Built as an **open-source educational project**  
Focused on learning, productivity, and student benefit.

---

## 📌 Final Note

This blueprint exists so that:
- The project can grow without confusion
- New contributors can onboard easily
- The logic remains clean and intentional

> Simple tools, built well, last the longest.