import pytesseract
import torch
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import numpy as np
from transformers import AutoProcessor, AutoModelForTokenClassification
import re
import os
import torchvision.transforms as transforms

# Initialize Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
custom_config = r'--oem 3 --psm 6 -l eng -c preserve_interword_spaces=1'

# Initialize LayoutLMv3
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device} for LayoutLMv3")

model_name = "microsoft/layoutlmv3-base"
processor = AutoProcessor.from_pretrained(model_name, apply_ocr=True)
model = AutoModelForTokenClassification.from_pretrained(model_name).to(device)

def extract_text_from_image(image_path):
    """Extract text from newspaper image using LayoutLMv3 for structure and Tesseract for text"""
    try:
        # Load the image
        image = Image.open(image_path)

        # Ensure image is in RGB format
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Extract text with Tesseract
        extracted_text = pytesseract.image_to_string(image)

        # Convert image to numpy array (LayoutLMv3 needs correct format)
        image_array = np.array(image)  # Convert PIL image to numpy

        # Process image with LayoutLMv3
        encoding = processor(images=image_array, text=extracted_text, return_tensors="pt", truncation=True)
        encoding = {k: v.to(device) for k, v in encoding.items()}

        with torch.no_grad():
            outputs = model(**encoding)

        return extracted_text

        print(extracted_text)

    except Exception as e:
        print(f"Error extracting text: {e}")
        import traceback
        traceback.print_exc()
        return f"Error extracting text: {str(e)}"
