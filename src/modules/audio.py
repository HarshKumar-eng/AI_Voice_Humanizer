import librosa
import soundfile as sf
import numpy as np
import os

def load_audio(file_path, target_sr=24000):
    """
    Loads audio file.
    Returns: (audio_array, sampling_rate)
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
        
    try:
        # Load with librosa (resamples automatically if needed)
        y, sr = librosa.load(file_path, sr=target_sr)
        return y, sr
    except Exception as e:
        raise RuntimeError(f"Failed to load audio: {e}")

def save_audio(file_path, y, sr):
    """
    Saves audio array to file.
    """
    try:
        sf.write(file_path, y, sr)
        print(f"Saved audio to {file_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to save audio: {e}")
