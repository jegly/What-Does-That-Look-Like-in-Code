#!/bin/bash
# setup.sh - Installation script for WDLIC

set -e

echo "========================================="
echo "WDLIC Setup - What Does That Look Like in Code"
echo "========================================="
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Check if Python 3.8+
required_version="3.8"
if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 8) else 1)"; then
    echo "Error: Python 3.8 or higher is required"
    exit 1
fi

echo "✓ Python version OK"
echo ""

# Install pip packages
echo "Installing Python dependencies..."
pip install --break-system-packages -q -r requirements.txt

echo "✓ Dependencies installed"
echo ""

# Download spaCy model
echo "Downloading spaCy language model..."
python3 -m spacy download en_core_web_sm

echo "✓ spaCy model downloaded"
echo ""

# Make main.py executable
chmod +x main.py

echo "========================================="
echo "✓ Setup complete!"
echo "========================================="
echo ""
echo "Try it out:"
echo "  python main.py \"A person decides whether to take a risk\""
echo ""
echo "Or run tests:"
echo "  python -m pytest tests/ -v"
echo ""
echo "For more examples, see README.md"
