# WhatsApp Vocabulary Bot

**Automate daily English vocabulary learning via WhatsApp!**

---

## Description
This bot sends **daily English vocabulary** to your WhatsApp number. Each day’s words are unique, and previously sent words are tracked automatically. It is perfect for learners who want to **improve their English consistently** with minimal effort.

---

## Features
- Sends **daily vocabulary** via WhatsApp using Twilio sandbox  
- Tracks previously sent words to **avoid repetition**  
- Generates vocabulary messages using an **AI API** (OpenAI, Hugging Face, Cohere, or mock data for testing)  
- Fully configurable via `.env` for API keys and phone numbers  
- Easy to run locally, ready for cloud deployment  

---

## Technology Stack
- Python 3.8+  
- Twilio WhatsApp API  
- AI API (OpenAI / Hugging Face / Cohere)  
- JSON for storing sent words  
- Virtual environment (`venv`) for dependency management  

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/whatsapp-vocab-bot.git
cd whatsapp-vocab-bot
