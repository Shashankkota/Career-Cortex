#!/usr/bin/env bash
# This script will exit immediately if a command fails
set -o errexit

echo "--- STARTING SIMPLIFIED BUILD SCRIPT ---"

# Upgrade pip for the system python
pip install --upgrade pip

# Force install the exact correct library versions directly
echo "--- Installing required packages ---"
pip install python-telegram-bot==20.6 spacy==3.5.3 textstat PyMuPDF python-dotenv requests

# Verify the installation by printing all installed packages and their versions
echo "--- Verifying installed packages (pip freeze) ---"
pip freeze

# Download the spaCy English model
echo "--- Downloading spaCy model ---"
python -m spacy download en_core_web_sm

echo "--- BUILD SCRIPT FINISHED SUCCESSFULLY ---"
