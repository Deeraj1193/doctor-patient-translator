import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def translate_text(text: str, source_language: str, target_language: str) -> str:
    if not GEMINI_API_KEY:
        return text  # fallback if no key

    prompt = f"""
    Translate the following text from {source_language} to {target_language}.
    Only return the translated text.

    Text:
    {text}
    """

    response = model.generate_content(prompt)
    return response.text.strip()


def summarize_conversation(conversation_text: str) -> str:
    if not GEMINI_API_KEY:
        return "Summary service not configured."

    prompt = f"""
    You are a medical assistant AI.
    Summarize the following doctor-patient conversation.

    Highlight:
    - Symptoms
    - Diagnoses
    - Medications
    - Follow-up instructions

    Conversation:
    {conversation_text}
    """

    response = model.generate_content(prompt)
    return response.text.strip()
