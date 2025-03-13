"""
Delta Headlines - News OCR & Broadcaster
A hackathon project that converts newspaper images into professional news broadcasts.
"""

from flask import Flask
from config import CONFIG
import os
import torch

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.update(CONFIG)
    
    # Create necessary directories
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['AUDIO_FOLDER'], exist_ok=True)
    
    # Import and register blueprints if needed
    # from .routes import main_bp
    # app.register_blueprint(main_bp)
    
    return app