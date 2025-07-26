# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# ✅ Telegram Bot Token (move this to .env for safety)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Hugging Face API Token
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# 🔐 Authorization headers for HuggingFace API
HF_HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

# For Resume Scoring (placeholder spam classifier)
# ✅ For Resume Scoring – Simulated with MultinomialNB-based model
ATS_SCORE_MODEL = "mrm8488/bert-tiny-finetuned-sms-spam-detection"
NER_MODEL = "dslim/bert-base-NER"





# ✅ Hugging Face model endpoints


# ✅ Telegram Bot Token (do not share publicly)
# TELEGRAM_BOT_TOKEN = '8289195596:AAHVNCFmgfvxVzPqhbpg99X23I9B650b9sQ'

# # ✅ HuggingFace Inference API Token
# HUGGINGFACE_API_TOKEN = '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'