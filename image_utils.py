import cv2
import numpy as np
import os

def enhance_image_for_ocr(image_path):
    """
    Apply advanced image preprocessing techniques to enhance
    newspaper images for better OCR results
    """
    # Read image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply unsharp masking for edge enhancement
    gaussian = cv2.GaussianBlur(gray, (0, 0), 3.0)
    unsharp_mask = cv2.addWeighted(gray, 1.5, gaussian, -0.5, 0)
    
    # Apply adaptive thresholding
    binary = cv2.adaptiveThreshold(
        unsharp_mask, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 11, 2
    )
    
    # Noise removal
    denoised = cv2.fastNlMeansDenoising(binary, None, 10, 7, 21)
    
    # Dilation to connect broken characters
    kernel = np.ones((1, 1), np.uint8)
    dilated = cv2.dilate(denoised, kernel, iterations=1)
    
    # Save preprocessed image temporarily
    temp_path = f"{os.path.splitext(image_path)[0]}_preprocessed.jpg"
    cv2.imwrite(temp_path, dilated)
    
    return temp_path

def detect_text_regions(image_path):
    """
    Detect regions in the newspaper that likely contain text
    using contour detection
    """
    # Read image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by area
    text_regions = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        area = w * h
        
        # Skip very small regions
        if area < 100:
            continue
            
        # Skip very large regions (likely images)
        if area > (image.shape[0] * image.shape[1]) / 4:
            continue
            
        # Calculate aspect ratio
        aspect_ratio = float(w) / h
        
        # Text regions typically have specific aspect ratios
        if 0.1 < aspect_ratio < 10:
            text_regions.append((x, y, w, h))
    
    return text_regions, image

def separate_headlines(image_path):
    """
    Attempt to identify headlines versus body text using
    size and position heuristics
    """
    # Detect text regions
    regions, image = detect_text_regions(image_path)
    
    # Sort regions by y-coordinate (top to bottom)
    regions.sort(key=lambda r: r[1])
    
    # Heuristic: Headlines are typically at the top and larger
    headlines = []
    body_text = []
    
    avg_height = sum(r[3] for r in regions) / len(regions) if regions else 0
    
    for x, y, w, h in regions:
        # If region is in top third of page and larger than average
        if y < image.shape[0] / 3 and h > avg_height * 1.2:
            headlines.append((x, y, w, h))
        else:
            body_text.append((x, y, w, h))
    
    return headlines, body_text