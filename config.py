import os

# Configuration settings
CONFIG = {
    # Application settings
    'DEBUG': True,
    'SECRET_KEY': os.environ.get('SECRET_KEY', 'delta-headlines-default-key'),
    'UPLOAD_FOLDER': 'static/uploads',
    'AUDIO_FOLDER': 'static/audio',
    'MAX_CONTENT_LENGTH': 16 * 1024 * 1024,  # 16MB max upload
    
    # OCR settings
    'TESSERACT_PATH': os.environ.get('TESSERACT_PATH', r"C:/Program Files/Tesseract-OCR/tesseract.exe"),
    'TESSERACT_CONFIG': r'--oem 3 --psm 6 -l eng -c preserve_interword_spaces=1',
    
    # LayoutLM settings
    'LAYOUTLM_MODEL': 'microsoft/layoutlmv3-base',
    
    # LLM settings
    'LLM_MODEL': 'google/flan-t5-large',
    'USE_FLOAT16': True,
    
    # TTS settings
    'TTS_VOICE': 'bm_fable',  # broadcaster male voice
    'TTS_SPEED': 1.0,         # normal speed
    
    # Summarization settings
    'SUMMARY_MAX_LENGTH': 300,
    'REPORT_MAX_LENGTH': 500
}