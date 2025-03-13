#!/bin/bash

# Delta Headlines - Hackathon Project Setup Script

# Colors for better visibility
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Delta Headlines Hackathon Project Setup ===${NC}"

# Create virtual environment
echo -e "${GREEN}Creating virtual environment...${NC}"
python -m venv venv

# Activate virtual environment
echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate  # For Linux/Mac
# Uncomment the line below for Windows
# .\venv\Scripts\activate

# Install dependencies
echo -e "${GREEN}Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements.txt

# Check for Tesseract installation
if command -v tesseract &> /dev/null; then
    echo -e "${GREEN}Tesseract is installed.${NC}"
else
    echo -e "${RED}Tesseract OCR is not installed.${NC}"
    echo -e "${BLUE}Please install Tesseract OCR:${NC}"
    echo "  - For Ubuntu: sudo apt install tesseract-ocr"
    echo "  - For macOS: brew install tesseract"
    echo "  - For Windows: Download from https://github.com/UB-Mannheim/tesseract/wiki"
    echo -e "${BLUE}After installation, update the TESSERACT_PATH in config.py${NC}"
fi

# Create necessary directories
echo -e "${GREEN}Creating project directories...${NC}"
mkdir -p static/uploads
mkdir -p static/audio

# Set environment variables
echo -e "${GREEN}Setting up environment variables...${NC}"
# Uncomment and modify the line below for production
# export SECRET_KEY="your-secure-secret-key"

echo -e "${BLUE}Setup complete!${NC}"
echo -e "${GREEN}To run the application:${NC}"
echo "  python app.py"
echo -e "${GREEN}Then navigate to:${NC} http://localhost:5000"