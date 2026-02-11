import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

print("TOKEN: ",HF_API_TOKEN)

BASE_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}


def call_hf(prompt):
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 200
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return f"HF API error: {response.text}"

    result = response.json()

    return result["choices"][0]["message"]["content"].strip()


def translate_text(text, source_language, target_language):
    prompt = f"Translate from {source_language} to {target_language}: {text}"
    return call_hf(prompt)


def summarize_conversation(conversation_text):
    prompt = f"Summarize this medical conversation:\n{conversation_text}"
    return call_hf(prompt)

def generate_summary_text(conversation_text: str) -> str:
    prompt = f"""
You are a clinical assistant generating a medical summary.

Summarize the following doctor-patient conversation.

STRICT RULES:
- DO NOT rewrite the entire conversation.
- DO NOT include dialogue format.
- DO NOT include names like Doctor or Patient.
- DO NOT use asterisks, markdown, or symbols.
- DO NOT say "Here is a summary" or similar.
- Output only a clean professional medical summary.
- Keep it concise (4-6 sentences maximum).

Conversation:
{conversation_text}
"""

    try:
        text = call_hf(prompt)

        # Extra cleanup safeguard
        text = text.replace("*", "")
        text = text.replace("Here is", "")
        text = text.replace("Here's", "")
        text = text.replace("---", "")

        return text.strip()

    except Exception:
        return "Summary generation failed."

