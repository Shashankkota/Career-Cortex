#!/usr/bin/env bash
# This script will exit immediately if a command fails
set -o errexit

echo "--- Starting a fresh build, ignoring cache ---"

# Force install the exact, correct versions of all libraries in one line
echo "Force installing correct library versions..."
pip install python-telegram-bot==20.6 spacy textstat PyMuPDF python-dotenv requests

echo "--- Library installation complete ---"

# Download the spaCy English model
echo "Downloading spaCy model..."
python -m spacy download en_core_web_sm

echo "--- Build script finished successfully ---"
