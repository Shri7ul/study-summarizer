import os
from dotenv import load_dotenv
import google.generativeai as genai

# load env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_easy_summary(chunk_text):
    """
    Generate student-friendly easy summary using Gemini
    """

    prompt = f"""
You are a helpful university study assistant.

Summarize the following lecture content in very easy language.

Rules:
- Use bullet points
- Focus on exam-relevant information
- Keep it short and clear
- Do NOT add extra explanations
- Do NOT use complex words

Lecture content:
{chunk_text}
"""

    response = model.generate_content(prompt)

    return response.text.strip()
