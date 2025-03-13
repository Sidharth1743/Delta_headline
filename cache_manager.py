"""
Cache manager for Delta Headlines application
Implements a simple in-memory cache and file-based caching
"""

import os
import json
import pickle
import hashlib
import time
import logging
from functools import wraps
from threading import Lock
import torch

logger = logging.getLogger("delta-headlines")

class CacheManager:
    """
    Cache manager that provides both memory and file-based caching
    to speed up expensive operations
    """
    
    def __init__(self, cache_dir="cache", ttl=3600):
        """
        Initialize the cache manager
        
        Args:
            cache_dir (str): Directory to store cached files
            ttl (int): Time to live in seconds for cached items
        """
        self.memory_cache = {}
        self.cache_dir = cache_dir
        self.ttl = ttl
        self.lock = Lock()
        
        # Create cache directory if it doesn't exist
        os.makedirs(self.cache_dir, exist_ok=True)
    
    def _get_cache_key(self, func_name, *args, **kwargs):
        """Generate a unique cache key based on function name and arguments"""
        # Create a string representation of the function and arguments
        key_parts = [func_name]
        
        # Add args and kwargs to key parts
        key_parts.extend([str(arg) for arg in args])
        key_parts.extend([f"{k}:{v}" for k, v in sorted(kwargs.items())])
        
        # Create a hash of the combined string
        key_string = "::".join(key_parts)
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def _get_cache_path(self, cache_key):
        """Get the file path for a cache key"""
        return os.path.join(self.cache_dir, f"{cache_key}.cache")
    
    def memory_cache_decorator(self, ttl=None):
        """Decorator for in-memory caching"""
        if ttl is None:
            ttl = self.ttl
            
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Generate cache key
                cache_key = self._get_cache_key(func.__name__, *args, **kwargs)
                
                # Check if result is in cache and not expired
                with self.lock:
                    if cache_key in self.memory_cache:
                        timestamp, result = self.memory_cache[cache_key]
                        if time.time() - timestamp < ttl:
                            logger.debug(f"Cache hit for {func.__name__}")
                            return result
                
                # Execute function if not in cache or expired
                result = func(*args, **kwargs)
                
                # Store result in cache
                with self.lock:
                    self.memory_cache[cache_key] = (time.time(), result)
                
                return result
            return wrapper
        return decorator
    
    def file_cache_decorator(self, ttl=None):
        """Decorator for file-based caching"""
        if ttl is None:
            ttl = self.ttl
            
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Generate cache key
                cache_key = self._get_cache_key(func.__name__, *args, **kwargs)
                cache_path = self._get_cache_path(cache_key)
                
                # Check if file cache exists and is not expired
                if os.path.exists(cache_path):
                    cache_time = os.path.getmtime(cache_path)
                    if time.time() - cache_time < ttl:
                        logger.debug(f"File cache hit for {func.__name__}")
                        try:
                            with open(cache_path, 'rb') as f:
                                return pickle.load(f)
                        except Exception as e:
                            logger.error(f"Error loading cache file: {e}")
                
                # Execute function if not in cache or expired
                result = func(*args, **kwargs)
                
                # Store result in file cache
                try:
                    with open(cache_path, 'wb') as f:
                        pickle.dump(result, f)
                except Exception as e:
                    logger.error(f"Error writing cache file: {e}")
                
                return result
            return wrapper
        return decorator
    
    def clear_memory_cache(self):
        """Clear all items from memory cache"""
        with self.lock:
            self.memory_cache = {}
        logger.info("Memory cache cleared")
    
    def clear_file_cache(self):
        """Clear all items from file cache"""
        for filename in os.listdir(self.cache_dir):
            if filename.endswith(".cache"):
                os.remove(os.path.join(self.cache_dir, filename))
        logger.info("File cache cleared")
    
    def clear_all_cache(self):
        """Clear both memory and file cache"""
        self.clear_memory_cache()
        self.clear_file_cache()

# Create a global instance of the cache manager
cache_manager = CacheManager()