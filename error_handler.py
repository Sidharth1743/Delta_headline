"""
Error handling middleware for Delta Headlines application
"""

import logging
import traceback
from functools import wraps
from flask import jsonify, request
import torch
logger = logging.getLogger("delta-headlines")

class ErrorHandler:
    """Custom error handler for the Delta Headlines application"""
    
    @staticmethod
    def handle_exceptions(func):
        """Decorator to wrap API endpoints and handle exceptions"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Log the error with request information
                logger.error(f"Exception in {func.__name__}: {str(e)}")
                logger.error(f"Request path: {request.path}")
                logger.error(f"Request method: {request.method}")
                logger.error(f"Request args: {request.args}")
                logger.error(f"Client IP: {request.remote_addr}")
                logger.error(traceback.format_exc())
                
                # Return appropriate error response
                return jsonify({
                    'status': 'error',
                    'message': str(e),
                    'error_type': e.__class__.__name__
                }), 500
        
        return wrapper
    
    @staticmethod
    def api_error_response(error_message, status_code=400):
        """Generate standard error response for API endpoints"""
        return jsonify({
            'status': 'error',
            'message': error_message
        }), status_code
    
    @staticmethod
    def log_request(request):
        """Log incoming request details for debugging"""
        logger.info(f"Request: {request.method} {request.path}")
        logger.info(f"Client IP: {request.remote_addr}")
        logger.info(f"User Agent: {request.user_agent}")