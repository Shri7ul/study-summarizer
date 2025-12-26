import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_easy_summary(chunk_text, exam_mode=False, language="English"):
    """
    Generate structured student-friendly summary
    """

    lang_instruction = (
        "Write the summary in Bangla." if language == "Bangla"
        else "Write the summary in simple English."
    )

    exam_instruction = (
        "Focus on exam-oriented answers. Use definition style and keywords."
        if exam_mode
        else "Focus on easy understanding and quick revision."
    )

    prompt = prompt = f"""
You are a university study assistant.

{lang_instruction}
{exam_instruction}

IMPORTANT OUTPUT RULES:
- Do NOT use markdown formatting
- Do NOT use symbols like ##, **, *
- Do NOT use bold, italics, or headings with #
- Write in plain text only
- Use simple bullets like "-" or "•"
- Keep language exam-copy friendly

Lecture content:
{chunk_text}
"""


    response = model.generate_content(prompt)
    return response.text.strip()
