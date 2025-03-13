# Code for convert summary text into audio
# Give input in the summarized_text in the main function
# Output will save in the same folder as output.extension

import torch
from kokoro import KPipeline
import soundfile as sf
import os
import uuid
import re

# Initialize Kokoro TTS pipeline
print("Initializing Kokoro TTS...")
pipeline = KPipeline(lang_code='a')  # Use 'a' for American English or 'b' for British English

def split_into_sentences(text):
    """Split text into sentences for better TTS processing"""
    # Split by common sentence delimiters
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s for s in sentences if s.strip()]

def text_to_speech(text, output_filename="output.wav", voice='bm_fable'):
    """
    Convert text to speech using Kokoro TTS.
    Saves the audio file in the same folder as the script.
    """
    try:
        # Split text into smaller chunks for better processing
        sentences = split_into_sentences(text)
        
        # Process each sentence
        all_audio = []
        for sentence in sentences:
            if not sentence.strip():
                continue
                
            # Generate audio for this sentence
            generator = pipeline(
                sentence, 
                voice=voice,  # Use selected voice
                speed=1.0     # Normal speed
            )
            
            # Collect audio data
            for _, _, audio in generator:
                all_audio.append(audio)
        
        # Combine all audio segments
        if all_audio:
            combined_audio = torch.cat(all_audio, dim=0).numpy()
            
            # Save the combined audio in the same folder as the script
            sf.write(output_filename, combined_audio, 24000)
            
            print(f"Audio saved as: {os.path.abspath(output_filename)}")
            return output_filename
        else:
            raise Exception("No audio was generated")
    
    except Exception as e:
        print(f"Error in TTS: {e}")
        import traceback
        traceback.print_exc()
        return None

# Example usage
if __name__ == "__main__":
    # Example summarized text
    summarized_text = "The government has announced new policies to improve healthcare. These policies aim to reduce costs and increase accessibility for all citizens."
    
    # Convert summarized text to audio and save in the same folder
    text_to_speech(summarized_text, output_filename="output.wav", voice='bm_fable')