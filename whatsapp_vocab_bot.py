import os
import json
from datetime import datetime
from dotenv import load_dotenv
from twilio.rest import Client
from openai import OpenAI

# ------------------ SETUP ------------------

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = os.getenv("TWILIO_WHATSAPP_FROM")
TO_WHATSAPP = os.getenv("MY_WHATSAPP")

VOCAB_FILE = "used_vocab.json"

ai_client = OpenAI(api_key=OPENAI_API_KEY)
twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

# ------------------ STORAGE ------------------

def load_used_vocab():
    if not os.path.exists(VOCAB_FILE):
        return []
    with open(VOCAB_FILE, "r") as f:
        return json.load(f)

def save_used_vocab(words):
    with open(VOCAB_FILE, "w") as f:
        json.dump(words, f, indent=2)

# ------------------ AI GENERATION ------------------

def generate_message(used_vocab):
    """
    Mock version for learning purposes (no API call)
    """
    today = datetime.now().strftime("%A, %d %B")
    
    # Sample vocab (make sure we skip already used ones)
    sample_vocab = [
        {"word": "resilient", "meaning": "able to recover quickly", "example": "She remained resilient after failure."},
        {"word": "articulate", "meaning": "express ideas clearly", "example": "He articulated his thoughts well."},
        {"word": "meticulous", "meaning": "very careful and precise", "example": "She is meticulous in her work."},
        {"word": "innovative", "meaning": "creative, new ideas", "example": "He proposed an innovative solution."},
        {"word": "tenacious", "meaning": "persistent, determined", "example": "She is tenacious in reaching her goals."}
    ]

    # Filter out already used words
    new_words = [v for v in sample_vocab if v["word"] not in used_vocab][:3]

    # Build message string
    message = f"Good morning! Today is {today}.\n\nStay consistent today 💪\n\n📘 Vocabulary:\n"
    for v in new_words:
        message += f"- {v['word'].capitalize()}: {v['meaning']}\n  Example: {v['example']}\n"
    
    return message


# ------------------ VOCAB EXTRACTION ------------------

def extract_vocab_words(text):
    vocab = []
    for line in text.split("\n"):
        line = line.strip()
        if line and ":" in line:
            word = line.split(":")[0].strip("123.- ").lower()
            if word.isalpha():
                vocab.append(word)
    return vocab[:3]

# ------------------ WHATSAPP SEND ------------------

def send_whatsapp(message):
    twilio_client.messages.create(
        body=message,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

# ------------------ MAIN ------------------

def main():
    used_vocab = load_used_vocab()

    message = generate_message(used_vocab)
    new_vocab = extract_vocab_words(message)

    updated_vocab = list(set(used_vocab + new_vocab))
    save_used_vocab(updated_vocab)

    send_whatsapp(message)

    print("✅ Message sent successfully")
    print("📘 New vocab added:", new_vocab)

if __name__ == "__main__":
    main()
