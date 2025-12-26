import google.generativeai as genai


def generate_questions(text, language="English"):
    prompt = f"""
Generate possible exam questions from the lecture content.

Rules:
- Plain text only
- Short questions
- Suitable for 2–5 marks
- Language: {language}

Lecture:
{text}
"""
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text.strip()
