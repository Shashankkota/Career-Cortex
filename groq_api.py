# groq_api.py
import os
import requests
import logging
from typing import Optional

# Configuration is now passed in, not loaded here
GROQ_API_URL = 'https://api.groq.com/openai/v1/chat/completions'

def call_groq_for_career_advice(user_question: str, resume_context: str, api_key: str) -> Optional[str]:
    """
    Calls the Groq API with resume context to answer user questions.
    The API key is passed directly to this function.
    """
    if not api_key:
        logging.error("Groq API key was not provided to the function.")
        return "Sorry, the career coach AI is currently unavailable due to a configuration issue."

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }

    system_prompt = (
        "You are an expert career coach and professional resume analyst. Your tone is helpful, encouraging, and sharp. "
        "Using the provided resume text as the sole source of truth, answer the user's question concisely. "
        "If the question is for general career advice, use your expertise. If the question is about the resume and the information isn't there, say so."
    )
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Here is the user's resume text:\n---BEGIN RESUME---\n{resume_context}\n---END RESUME---\n\nUser's question: {user_question}"}
    ]
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": messages,
        "max_tokens": 1024,
        "temperature": 0.4
    }

    try:
        resp = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Groq API error: {e}")
        return "Sorry, I encountered an issue while trying to get an answer. Please try again."