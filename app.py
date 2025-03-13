"""
Delta Headlines - Main Application
News OCR & Broadcasting System for Hackathon
"""

from flask import Flask, render_template, request, jsonify, send_file, url_for, redirect
import os
import logging
from werkzeug.utils import secure_filename
import time
import uuid
import traceback
from datetime import datetime
import torch
# Import configuration
from config import CONFIG

# Import our modules
from ocr_module import extract_text_from_image
from summarizer import summarize_text
from report_generator import generate_report
from tts_module import text_to_speech
from image_utils import enhance_image_for_ocr

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("delta-headlines")

# Initialize Flask application
app = Flask(__name__)
app.config.update(CONFIG)

# Create necessary folders
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    """Render the main application page"""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    """Process uploaded newspaper image"""
    start_time = time.time()
    logger.info("Starting image processing request")
    
    try:
        if 'file' not in request.files:
            logger.warning("No file part in request")
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            logger.warning("No selected file")
            return jsonify({'error': 'No selected file'}), 400
        
        if file:
            # Generate unique filename
            original_filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{str(uuid.uuid4())}{os.path.splitext(original_filename)[1]}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            logger.info(f"File saved to {filepath}")
            
            # Record processing stages timing
            stage_times = {}
            
            # Extract text using OCR
            logger.info("Starting OCR text extraction")
            stage_start = time.time()
            extracted_text = extract_text_from_image(filepath)
            stage_times['ocr'] = time.time() - stage_start
            logger.info(f"OCR completed in {stage_times['ocr']:.2f} seconds")
            
            # Summarize the extracted text
            logger.info("Starting text summarization")
            stage_start = time.time()
            summarized_text = summarize_text(extracted_text)
            stage_times['summarize'] = time.time() - stage_start
            logger.info(f"Summarization completed in {stage_times['summarize']:.2f} seconds")
            
            # Generate news report
            logger.info("Starting news report generation")
            stage_start = time.time()
            news_report = generate_report(summarized_text)
            stage_times['report'] = time.time() - stage_start
            logger.info(f"Report generation completed in {stage_times['report']:.2f} seconds")
            
            # Convert to speech
            logger.info("Starting text-to-speech conversion")
            stage_start = time.time()
            audio_filename = text_to_speech(news_report, app.config['AUDIO_FOLDER'])
            stage_times['tts'] = time.time() - stage_start
            logger.info(f"TTS completed in {stage_times['tts']:.2f} seconds")
            
            # Calculate total processing time
            total_time = time.time() - start_time
            logger.info(f"Total processing completed in {total_time:.2f} seconds")
            
            # Create response
            response = {
                'status': 'success',
                'original_text': extracted_text,
                'summarized_text': summarized_text,
                'news_report': news_report,
                'audio_file': f"/static/audio/{audio_filename}",
                'processing_times': {
                    'ocr': f"{stage_times['ocr']:.2f}s",
                    'summarize': f"{stage_times['summarize']:.2f}s",
                    'report': f"{stage_times['report']:.2f}s",
                    'tts': f"{stage_times['tts']:.2f}s",
                    'total': f"{total_time:.2f}s"
                }
            }
            
            return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        logger.error(traceback.format_exc())
        return jsonify({
            'error': f"Processing failed: {str(e)}",
            'status': 'error'
        }), 500

@app.route('/audio/<filename>')
def audio(filename):
    """Serve audio files"""
    try:
        return send_file(os.path.join(app.config['AUDIO_FOLDER'], filename))
    except Exception as e:
        logger.error(f"Error serving audio file: {str(e)}")
        return jsonify({'error': f"File not found: {str(e)}"}), 404

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'components': {
            'ocr': True,
            'summarizer': True,
            'report_generator': True,
            'tts': True
        }
    })

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    """Handle 500 errors"""
    logger.error(f"Server error: {str(e)}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    logger.info("Starting Delta Headlines application")
    app.run(debug=CONFIG['DEBUG'], host='0.0.0.0', port=5000)