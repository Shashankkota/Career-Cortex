#!/usr/bin/env bash
# Exit on error to ensure a clean failure if something goes wrong
set -o errexit

echo "--- STARTING ELITE DEBUG BUILD SCRIPT ---"

# Step 1: Create a fresh, isolated virtual environment
echo "--- Creating a fresh virtual environment in ./venv ---"
python -m venv venv

# Step 2: Activate the virtual environment
source venv/bin/activate
echo "--- Virtual environment activated. ---"

# Step 3: Upgrade pip and force install the exact correct library versions
echo "--- Force installing correct library versions ---"
pip install --upgrade pip
pip install python-telegram-bot==20.6 spacy==3.5.3 textstat PyMuPDF python-dotenv requests

# Step 4: Verify the installation by printing all installed packages and their versions
echo "--- VERIFICATION STEP: Verifying installed packages ---"
pip freeze
echo "--- VERIFICATION COMPLETE ---"

# Step 5: Download the spaCy English model
echo "--- Downloading spaCy model ---"
python -m spacy download en_core_web_sm

echo "--- BUILD SCRIPT FINISHED SUCCESSFULLY ---"
