# import os
# import asyncio
# import logging
# from telegram import Update, Document
# from telegram.ext import Application, MessageHandler, filters, ContextTypes, CommandHandler
# from config import TELEGRAM_BOT_TOKEN
# from scorer import score_resume
# from resume_parser import extract_text_from_pdf
# from utils import build_output_message

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# DOWNLOAD_DIR = "downloads"
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "👋 Hi! Send me your resume as a PDF and I’ll review it with AI-powered feedback."
#     )

# async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     try:
#         doc: Document = update.message.document
#         filename = doc.file_name

#         if not filename.lower().endswith(".pdf"):
#             await update.message.reply_text("❌ Please upload your resume in PDF format only.")
#             return

#         for attempt in range(3):
#             try:
#                 tg_file = await doc.get_file()
#                 break
#             except Exception as e:
#                 logger.warning(f"Timeout while downloading file. Attempt {attempt + 1}/3")
#                 await asyncio.sleep(2)
#         else:
#             await update.message.reply_text("❌ Failed to download the file. Please try again.")
#             return

#         local_path = os.path.join(DOWNLOAD_DIR, filename)
#         await tg_file.download_to_drive(local_path)

#         await update.message.reply_text("📄 Resume received. Analyzing...")

#         text = extract_text_from_pdf(local_path)

#         if not text:
#             await update.message.reply_text("❌ Couldn’t extract text from your resume. Please ensure it’s not image-based.")
#             return

#         # Use your scorer to get the full analysis
#         analysis_result = score_resume(text)

#         # Build the message using the structured data from the scorer
#         output_message = build_output_message(
#             score=analysis_result["score"],
#             suggestions=analysis_result["suggestions"],
#             strengths=analysis_result["strengths"],
#             improvements=analysis_result["improvements"]
#         )

#         await update.message.reply_text(output_message, parse_mode='HTML')

#     except Exception as e:
#         logger.error(f"❌ Error: {e}")
#         await update.message.reply_text("❌ Something went wrong while processing your resume.")


# def main():
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

#     logger.info("🚀 Bot started...")
#     application.run_polling()

# if __name__ == '__main__':
#     main()

#other
# import os
# import logging
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# from config import TELEGRAM_BOT_TOKEN
# from resume_parser import extract_text_from_pdf
# from scorer import professional_analysis
# from utils import build_professional_output

# # Enable logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# DOWNLOAD_DIR = "downloads"
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Sends a welcome message."""
#     await update.message.reply_text(
#         "👋 Welcome to the Advanced Resume Analyzer!\n\n"
#         "Please upload your resume as a PDF file. I will conduct a detailed analysis and provide professional feedback to help you improve it."
#     )

# async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     """Receives a resume, analyzes it, and sends back the report."""
#     try:
#         doc = update.message.document
#         if not doc or not doc.file_name.lower().endswith(".pdf"):
#             await update.message.reply_text("Please upload your resume in PDF format only.")
#             return

#         await update.message.reply_text("📄 Resume received. Performing advanced analysis... This may take a moment.")
        
#         tg_file = await doc.get_file()
#         local_path = os.path.join(DOWNLOAD_DIR, f"{update.message.from_user.id}_resume.pdf")
#         await tg_file.download_to_drive(local_path)

#         resume_text = extract_text_from_pdf(local_path)
#         if not resume_text:
#             await update.message.reply_text("❌ Couldn’t extract text from your resume. Please ensure it’s not image-based and try again.")
#             return

#         # Perform the full professional analysis
#         analysis_data = professional_analysis(resume_text)
        
#         # Build the professional-looking output message
#         output_message = build_professional_output(analysis_data)
        
#         await update.message.reply_text(output_message, parse_mode='HTML')

#     except Exception as e:
#         logger.error(f"Error in handle_document: {e}", exc_info=True)
#         await update.message.reply_text("An error occurred while processing your resume. Please try again.")

# def main():
#     """Run the bot."""
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.Document.PDF, handle_document))

#     logger.info("🚀 Advanced Resume Bot started...")
#     application.run_polling()

# if __name__ == '__main__':
#     main()
# import os
# import logging
# from dotenv import load_dotenv
# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     MessageHandler,
#     CallbackQueryHandler,
#     ConversationHandler,
#     ContextTypes,
#     filters,
# )

# from resume_parser import extract_text_from_pdf
# from scorer import professional_analysis
# from utils import build_professional_output
# from groq_api import call_groq_for_career_advice

# # Load environment variables
# load_dotenv()
# TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# # Enable logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # States for conversation
# AWAIT_RESUME, QNA_SESSION = range(2)
# DOWNLOAD_DIR = "downloads"
# os.makedirs(DOWNLOAD_DIR, exist_ok=True)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Starts the conversation and asks for the 'Start Analysis' button press."""
#     welcome_text = """
# *What can this bot do?*

# *INTRODUCING THE ELITE RESUME SCREENER!* 🤖
# By Shashank

# Your one-stop solution for perfecting your resume for Applicant Tracking Systems (ATS). With this bot, you can:

# 1. Get a Professional, Detailed ATS Score
# 2. Analyze Your Resume's Impact & Keywords
# 3. Receive Actionable Feedback for Improvement

# Perfecting your resume has never been easier. Press the button below to begin!
#     """
#     keyboard = [[InlineKeyboardButton("▶️ Start Analysis", callback_data='start_analysis')]]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')
#     return AWAIT_RESUME


# async def prompt_for_resume(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Handles the button press and prompts for the PDF."""
#     query = update.callback_query
#     await query.answer()
#     await query.message.reply_text("Great! Please upload your resume as a single PDF file to begin the analysis.")
#     return AWAIT_RESUME


# async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Analyzes the resume and transitions to the Q&A state."""
#     try:
#         doc = update.message.document
#         if not doc or not doc.file_name.lower().endswith(".pdf"):
#             await update.message.reply_text("Please upload in PDF format only.")
#             return AWAIT_RESUME

#         await update.message.reply_text("📄 Resume received. Performing advanced analysis...")
#         tg_file = await doc.get_file()
#         local_path = os.path.join(DOWNLOAD_DIR, f"{update.message.from_user.id}_resume.pdf")
#         await tg_file.download_to_drive(local_path)

#         resume_text = extract_text_from_pdf(local_path)
#         if not resume_text:
#             await update.message.reply_text("❌ Couldn’t extract text from the PDF. Please try again.")
#             return AWAIT_RESUME

#         # Store resume text for the Q&A session
#         context.user_data['resume_text'] = resume_text

#         analysis_data = professional_analysis(resume_text)
#         output_message = build_professional_output(analysis_data)
#         await update.message.reply_text(output_message, parse_mode='HTML')
        
#         # Transition to the Q&A state
#         return QNA_SESSION

#     except Exception as e:
#         logger.error(f"Error in handle_document: {e}", exc_info=True)
#         await update.message.reply_text("An error occurred. Please try again by sending /start.")
#         return ConversationHandler.END


# async def handle_qna(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Handles user questions during the Q&A session."""
#     user_question = update.message.text
#     resume_text = context.user_data.get('resume_text')

#     if not resume_text:
#         await update.message.reply_text("It seems I've lost your resume context. Please start over with /start.")
#         return ConversationHandler.END

#     await update.message.reply_text("🤔 Thinking...")
    
#     answer = call_groq_for_career_advice(user_question, resume_text)
#     await update.message.reply_text(answer)
    
#     return QNA_SESSION


# async def end_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
#     """Ends the conversation."""
#     await update.message.reply_text("Happy to help! The chat session has ended. Send /start to analyze another resume.")
#     context.user_data.clear()
#     return ConversationHandler.END


# def main() -> None:
#     """Run the bot."""
#     if not TELEGRAM_BOT_TOKEN:
#         logger.error("TELEGRAM_BOT_TOKEN not found! Please set it in your .env file.")
#         return

#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).read_timeout(30).write_timeout(30).build()

#     # Setup ConversationHandler
#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             AWAIT_RESUME: [
#                 CallbackQueryHandler(prompt_for_resume, pattern='^start_analysis$'),
#                 MessageHandler(filters.Document.PDF, handle_document)
#             ],
#             QNA_SESSION: [
#                 CommandHandler("end", end_conversation),
#                 MessageHandler(filters.TEXT & ~filters.COMMAND, handle_qna)
#             ],
#         },
#         fallbacks=[CommandHandler("end", end_conversation), CommandHandler("start", start)],
#     )

#     application.add_handler(conv_handler)
    
#     logger.info("🚀 AI Career Coach Bot started...")
#     application.run_polling()


# if __name__ == '__main__':
#     main()

import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# --- Explicitly find and load the .env file ---
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY") # Load the Groq key here

# --- Environment Variable Debugger ---
# This will run once when you start the bot.
print("--- Environment Variable Debugger ---")
print(f"Looking for .env file at: {dotenv_path}")
if os.path.exists(dotenv_path):
    print("✅ .env file FOUND.")
    with open(dotenv_path, 'r') as f:
        print("\n--- Contents of .env file: ---")
        print(f.read())
        print("------------------------------")
else:
    print("❌ .env file NOT FOUND at the expected path.")

print(f"TELEGRAM_BOT_TOKEN loaded: {'Yes' if TELEGRAM_BOT_TOKEN else 'No'}")
print(f"GROQ_API_KEY loaded: {'Yes' if GROQ_API_KEY else 'No'}")
print("------------------------------------")
# --- End Debugging Step ---

from resume_parser import extract_text_from_pdf
from scorer import professional_analysis
from utils import build_professional_output
from groq_api import call_groq_for_career_advice

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

MAIN_KEYBOARD = [["📄 Upload Resume"], ["💬 Ask a Question (Q&A)"], ["❌ End Session"]]
REPLY_MARKUP = ReplyKeyboardMarkup(MAIN_KEYBOARD, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    welcome_text = """
*Welcome to the Elite Resume Screener!* 🤖
By Shashank

I am an advanced AI career coach designed to help you perfect your resume.

*How to use me:*
1.  Click `📄 Upload Resume` to get a detailed analysis.
2.  After your analysis, click `💬 Ask a Question (Q&A)` to start a chat about your resume.

Press a button below to begin!
    """
    await update.message.reply_text(welcome_text, reply_markup=REPLY_MARKUP, parse_mode='Markdown')

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        doc = update.message.document
        await update.message.reply_text("📄 Resume received. Performing elite analysis...", reply_markup=REPLY_MARKUP)
        tg_file = await doc.get_file()
        local_path = os.path.join(DOWNLOAD_DIR, f"{update.message.from_user.id}_resume.pdf")
        await tg_file.download_to_drive(local_path)
        resume_text = extract_text_from_pdf(local_path)
        context.user_data['resume_text'] = resume_text
        analysis_data = professional_analysis(resume_text)
        output_message = build_professional_output(analysis_data)
        await update.message.reply_text(output_message, parse_mode='HTML', reply_markup=REPLY_MARKUP)
    except Exception as e:
        logger.error(f"Error in handle_document: {e}", exc_info=True)
        await update.message.reply_text("An error occurred during analysis.", reply_markup=REPLY_MARKUP)

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if user_text == "📄 Upload Resume":
        await update.message.reply_text("Please send your PDF resume now.", reply_markup=REPLY_MARKUP)
    elif user_text == "💬 Ask a Question (Q&A)":
        if 'resume_text' in context.user_data:
            await update.message.reply_text("I'm ready! What would you like to ask?", reply_markup=REPLY_MARKUP)
        else:
            await update.message.reply_text("Please upload a resume first.", reply_markup=REPLY_MARKUP)
    elif user_text == "❌ End Session":
        await end_session(update, context)
    else:
        if 'resume_text' in context.user_data:
            await update.message.reply_text("🤔 Thinking...")
            # ▼▼▼ THIS IS THE CORRECTED LINE ▼▼▼
            answer = call_groq_for_career_advice(user_text, context.user_data['resume_text'], GROQ_API_KEY)
            # ▲▲▲ END OF CORRECTION ▲▲▲
            await update.message.reply_text(answer, reply_markup=REPLY_MARKUP)
        else:
            await update.message.reply_text("I'm not sure how to respond. Please select an option from the menu.", reply_markup=REPLY_MARKUP)

async def end_session(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text("Your session has been cleared. Send /start to begin again!", reply_markup=REPLY_MARKUP)

def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        logger.error("CRITICAL: TELEGRAM_BOT_TOKEN not found! The bot cannot start.")
        return

    application = Application.builder().token(TELEGRAM_BOT_TOKEN).read_timeout(30).write_timeout(30).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("end", end_session))
    application.add_handler(MessageHandler(filters.Document.PDF, handle_document))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    logger.info("🚀 AI Career Coach Bot with persistent menu started...")
    application.run_polling()

if __name__ == '__main__':
    main()