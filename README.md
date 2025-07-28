
🚀 Career Cortex 🤖 – An Elite AI Resume Coach


> A sophisticated Telegram bot that functions as a personal AI career coach — delivering elite-level ATS scoring and detailed, actionable feedback to perfect your resume.


🌟 Overview

In today’s competitive job market, your resume must appeal not just to human recruiters but also to Applicant Tracking Systems (ATS) that screen resumes automatically. Career Cortex bridges this gap.

Unlike simple keyword checkers, this intelligent coach applies an*expert-informed, multi-dimensional rubric to assess your resume. After analysis, it evolves into a conversational AI that allows personalized Q\&A based on your resume content.)

✨ Key Features

 ✅ Elite 100-Point ATS Score
  Comprehensive scoring system focused on **Structure**, **Impact**, and **Skills**.

 💡Per-Bullet Impact Analysis
  Evaluates every experience bullet for action verbs, quantified metrics, and clarity.

 🧠 Tiered Skill Classification
  Categorizes technical skills as Advanced, Core, or Foundational to assess depth.

 ✍️ Professional Writing Style Feedback
  Scores for readability, removes clichés, and ensures verb tense consistency.

 🤖 AI Career Q\&A Session
  Powered by Groq (Llama3) – offers intelligent, resume-specific career guidance via Telegram.

 🌐 24/7 Availability
  Cloud-deployed via webhook-based architecture for instant and persistent response handling.

---
 🛠️ Tech Stack

| Category           | Technology / Library                        |
| ------------------ | ------------------------------------------- |
| **Backend**        | Python 3.11                                 |
| **Bot Framework**  | `python-telegram-bot`                       |
| **NLP & Analysis** | `spaCy`, `textstat`                         |
| **PDF Parsing**    | `PyMuPDF`                                   |
| **Generative AI**  | Groq API (Llama3 8B)                        |
| **Deployment**     | Docker, Fly.io (or any webhook-ready cloud) |

---

 🚀 Getting Started

Follow these instructions to set up the project locally for development/testing:

✅ Prerequisites

* Python 3.10 or higher
* `pip` package manager
* Telegram Bot Token from [@BotFather](https://t.me/BotFather)
* API key from [Groq](https://groq.com/)



📦 Installation

1. Clone the Repository:

   git clone https://github.com/Shashankkota/Resume-Screening-Bot.git
   cd Resume-Screening-Bot
   

2. Set up Virtual Environment:

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install Dependencies:

   pip install -r requirements.txt

4. Download spaCy Model:

   python -m spacy download en_core_web_sm



⚙️ Configuration

1. Create a `.env` file in the root directory:

   TELEGRAM_BOT_TOKEN=your_telegram_token_here
   GROQ_API_KEY=your_groq_api_key_here

🧪 Running the Bot Locally

Start the bot in development mode (using polling):

python bot.py
