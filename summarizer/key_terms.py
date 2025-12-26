import google.generativeai as genai


def extract_key_terms(text):
    prompt = f"""
Extract important technical terms from the following lecture text.

Rules:
- Plain text only
- No markdown
- Bullet with "-"

Text:
{text}
"""
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text.strip()
