"""
Test script to verify individual components of the Delta Headlines system
Run this script to test specific modules before running the full application
"""

import argparse
import os
from PIL import Image
import time
import torch

def test_ocr(image_path):
    """Test the OCR module on a sample image"""
    from ocr_module import extract_text_from_image
    
    print(f"Testing OCR on image: {image_path}")
    start_time = time.time()
    
    extracted_text = extract_text_from_image(image_path)
    
    elapsed_time = time.time() - start_time
    print(f"OCR completed in {elapsed_time:.2f} seconds")
    
    print("-" * 50)
    print("Extracted Text:")
    print("-" * 50)
    print(extracted_text)
    print("-" * 50)
    
    return extracted_text

def test_summarizer(text=None, text_file=None):
    """Test the summarizer module with sample text"""
    from summarizer import summarize_text
    
    if text_file and os.path.exists(text_file):
        with open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
    
    if not text:
        text = """The United Nations Security Council met yesterday to discuss the ongoing crisis in Eastern Europe. 
        Representatives from 15 member states debated potential resolutions for the conflict that has displaced over 
        2 million civilians in the past month. The Secretary-General emphasized the urgent need for humanitarian aid 
        and called for an immediate ceasefire. Meanwhile, neighboring countries have reported a surge in refugee 
        arrivals, straining resources and creating challenges for border management. Aid organizations are mobilizing 
        to provide shelter, food, and medical assistance to those affected. Economic sanctions have been proposed 
        against the aggressor state, with mixed reactions from Council members."""
    
    print("Testing summarizer...")
    start_time = time.time()
    
    summary = summarize_text(text)
    
    elapsed_time = time.time() - start_time
    print(f"Summarization completed in {elapsed_time:.2f} seconds")
    
    print("-" * 50)
    print("Original Text Length:", len(text))
    print("Summary Length:", len(summary))
    print("-" * 50)
    print("Summary:")
    print("-" * 50)
    print(summary)
    print("-" * 50)
    
    return summary

def test_report_generator(summary=None):
    """Test the report generator module with a sample summary"""
    from report_generator import generate_report
    
    if not summary:
        summary = """The UN Security Council met to discuss the Eastern European crisis that has displaced 2 million 
        civilians. The Secretary-General called for humanitarian aid and an immediate ceasefire. Neighboring countries 
        are struggling with refugee management while aid organizations provide assistance. Economic sanctions against 
        the aggressor state received mixed reactions from Council members."""
    
    print("Testing report generator...")
    start_time = time.time()
    
    report = generate_report(summary)
    
    elapsed_time = time.time() - start_time
    print(f"Report generation completed in {elapsed_time:.2f} seconds")
    
    print("-" * 50)
    print("Report:")
    print("-" * 50)
    print(report)
    print("-" * 50)
    
    return report

def test_tts(text=None):
    """Test the text-to-speech module with sample text"""
    from tts_module import text_to_speech
    
    if not text:
        text = """BREAKING: DIPLOMATIC BREAKTHROUGH IN EASTERN EUROPE
        
        In a significant development, peace talks have yielded a breakthrough in the Eastern European conflict. 
        Negotiators announced a framework for ceasefire implementation starting tomorrow.
        
        This is Delta Headlines reporting."""
    
    print("Testing text-to-speech...")
    output_folder = "static/audio"
    os.makedirs(output_folder, exist_ok=True)
    
    start_time = time.time()
    
    audio_file = text_to_speech(text, output_folder)
    
    elapsed_time = time.time() - start_time
    print(f"TTS completed in {elapsed_time:.2f} seconds")
    
    print("-" * 50)
    print(f"Audio file created: {audio_file}")
    print(f"Full path: {os.path.join(output_folder, audio_file)}")
    print("-" * 50)
    
    return audio_file

def test_full_pipeline(image_path):
    """Test the complete pipeline from image to audio"""
    print("=" * 50)
    print("TESTING FULL PIPELINE")
    print("=" * 50)
    
    # Test OCR
    extracted_text = test_ocr(image_path)
    
    # Test summarization
    summary = test_summarizer(extracted_text)
    
    # Test report generation
    report = test_report_generator(summary)
    
    # Test TTS
    audio_file = test_tts(report)
    
    print("\nFull pipeline test completed!")
    print(f"Final audio output: {audio_file}")

def main():
    parser = argparse.ArgumentParser(description="Test Delta Headlines components")
    parser.add_argument("--component", choices=["ocr", "summarizer", "report", "tts", "full"], 
                      default="full", help="Component to test")
    parser.add_argument("--image", default=None, help="Path to newspaper image for OCR testing")
    parser.add_argument("--text", default=None, help="Path to text file for summarizer testing")
    
    args = parser.parse_args()
    
    if args.component in ["ocr", "full"] and not args.image:
        print("Error: Image path is required for OCR testing")
        print("Example: python test_components.py --component ocr --image sample_newspaper.jpg")
        return
    
    if args.component == "ocr":
        test_ocr(args.image)
    elif args.component == "summarizer":
        test_summarizer(text_file=args.text)
    elif args.component == "report":
        summary = test_summarizer(text_file=args.text)
        test_report_generator(summary)
    elif args.component == "tts":
        if args.text:
            with open(args.text, 'r', encoding='utf-8') as f:
                text = f.read()
            test_tts(text)
        else:
            test_tts()
    elif args.component == "full":
        test_full_pipeline(args.image)

if __name__ == "__main__":
    main()