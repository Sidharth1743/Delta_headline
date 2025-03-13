import re
import ollama  # Import the Ollama library

def clean_text(text):
    """Removes OCR-related errors, extra spaces, and formatting issues."""
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces/newlines
    text = re.sub(r"‘|’", "'", text)  # Normalize single quotes
    text = re.sub(r"“|”", '"', text)  # Normalize double quotes
    text = re.sub(r"—", "-", text)  # Normalize dashes
    return text.strip()

def summarize_text(text, max_length=150):
    """Summarizes the input text using Ollama."""
    try:
        text = clean_text(text)  # Preprocess text

        # Skip summarization if text is too short
        if len(text.split()) < 30:
            return text  

        # Ollama prompt format
        prompt = f"Summarize the following news article in a clear and concise way:\n\n{text}"

        # Use Ollama to generate the summary
        response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])

        # Extract the summary text
        summary = response["message"]["content"]

        return summary

    except Exception as e:
        print(f"Error in summarization: {e}")
        return f"Error during summarization: {str(e)}"
