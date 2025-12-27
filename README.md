# 📘 Study Summarizer

**Study Summarizer** is a student-focused AI tool that converts **PPTX and PDF study materials** into **easy, exam-ready summaries** within minutes.

Instead of spending 20–30 minutes reading slides or notes, students can get a **5-minute digest** designed for quick understanding and revision.

This project is built with simplicity, usefulness, and real student needs in mind.

---

## 🎯 Key Features

- 📂 Upload **PPTX or PDF** study materials
- 📄 **Preview or Full Summary** mode
- 🎯 **Exam-Focused Summary** option
- 🌍 **English & Bangla** language support
- 📌 **Important Key Terms extraction**
- ✍️ **Possible Exam Question generator**
- ⚡ **Smart Cache System** (saves API usage)
- ⬇️ Download summary as `.txt`
- 🖥️ Clean and simple **Streamlit UI**
- 🧠 Powered by **Gemini 2.5 Flash**

---

## 🧠 How It Works (Pipeline)
```yaml

PPTX / PDF
↓
Text Extraction
↓
Cleaning & Formatting
↓
Smart Chunking
↓
AI Summarization (Gemini)
↓
Final Study Notes

The system is modular, easy to extend, and optimized to reduce unnecessary API calls.
```
---

## 🛠️ Tech Stack

- **Python 3.10**
- **Streamlit** – UI
- **Gemini 2.5 Flash** – AI summarization
- **python-pptx** – PPTX reader
- **pdfplumber** – PDF reader
- **python-dotenv** – Environment variables

---

## ⚙️ Installation & Run

### 1️⃣ Create Environment
```bash
conda create -n study-summarizer python=3.10 -y
```
```bash
conda activate study-summarizer
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Add API Key
Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```
4️⃣ Run the App
```bash
python -m streamlit run app.py
```

## 🎓 Use Cases
- University lecture slides summarization

- Exam revision notes

- Last-minute study preparation

- Understanding complex topics easily

- Bangla explanation for better clarity

## 🔒 API & Cache Note
- To protect free API limits:

- Preview mode summarizes only the first section

- Cache system avoids repeated API calls for the same file

## 🌱 Open Source & Purpose
This project is:

- ✅ Open Source

- 🎓 Built for educational purposes

- 🤝 Free to use, modify, and learn from

- Contributions, ideas, and improvements are always welcome.

👤 Author  
**InHuman**  
Built with ❤️ for students and learning.

📜 License  
This project is open-source and intended strictly for educational and learning purposes.