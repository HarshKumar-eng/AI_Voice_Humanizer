import librosa
import numpy as np
import soundfile as sf
import parselmouth
from parselmouth.praat import call
import os
import tempfile
from pydub import AudioSegment

class AudioManipulator:
    def __init__(self):
        pass

    def apply_preset(self, audio_path, preset, words_alignment):
        """
        Applies emotion, tempo, and pitch changes.
        Returns path to processed temporary file.
        """
        # 1. Load original
        sound = parselmouth.Sound(audio_path)
        
        # 2. Apply Presets using Praat "Change speaker..."
        # Arguments: min_pitch, max_pitch, formant_shift_ratio, pitch_median_shift_ratio, pitch_range_scale, duration_factor
        # formant_shift_ratio = 1.0 (Preserve voice identity)
        # pitch_median_shift_ratio = 2^(semitones/12)
        # pitch_range_scale = preset.pitch_variance
        # duration_factor = 1 / preset.speed_factor

        pitch_median_ratio = 2 ** (preset.pitch_shift / 12.0)
        pitch_range_ratio = preset.pitch_variance
        duration_factor = 1.0 / preset.speed_factor
        
        try:
            # high-quality manipulation preserving formants
            sound = call(sound, "Change speaker...", 75, 600, 1.0, pitch_median_ratio, pitch_range_ratio, duration_factor)
        except Exception as e:
            print(f"Praat error: {e}")
            raise e

        # 3. Save to temp
        temp_fd, temp_path = tempfile.mkstemp(suffix='.wav')
        os.close(temp_fd)
        sound.save(temp_path, 'WAV')
        
        # 5. Insert Pauses / Breath (using Pydub)
        final_audio = AudioSegment.from_wav(temp_path)
        
        # Clean up temp
        os.remove(temp_path)
        
        return final_audio

    def insert_pauses(self, audio_segment, alignment, preset):
        # Implementation to slice breath/pause based on alignment
        # This is complex to do blindly without reconstructing the audio.
        # For MVP: We just return the manipulated audio
        return audio_segment
