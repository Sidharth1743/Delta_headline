# tts_module.py - Text-to-speech using Kokoro
import torch
from kokoro import KPipeline
import soundfile as sf
import os
import uuid
import re

# Initialize Kokoro TTS pipeline
print("Initializing Kokoro TTS...")
pipeline = KPipeline(lang_code='a')  # 'a' for American English

def split_into_sentences(text):
    """Split text into sentences for better TTS processing"""
    # Split by common sentence delimiters
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s for s in sentences if s.strip()]

def text_to_speech(text, output_folder, voice='ef_dora'):
    """
    Convert text to speech using Kokoro TTS
    Returns the filename of the generated audio
    """
    try:
        # Create unique audio filename
        audio_filename = f"{str(uuid.uuid4())}.wav"
        audio_path = os.path.join(output_folder, audio_filename)
        
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
                voice=voice,  # Use the specified voice
                speed=1.0     # Normal speed
            )
            
            # Collect audio data
            for _, _, audio in generator:
                all_audio.append(audio)
        
        # Combine all audio segments
        if all_audio:
            combined_audio = torch.cat(all_audio, dim=0).numpy()
            
            # Save the combined audio
            sf.write(audio_path, combined_audio, 24000)
            
            return audio_filename
        else:
            raise Exception("No audio was generated")
    
    except Exception as e:
        print(f"Error in TTS: {e}")
        import traceback
        traceback.print_exc()
        return None