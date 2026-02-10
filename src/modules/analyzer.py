import parselmouth
import numpy as np
import librosa

class AudioAnalyzer:
    def __init__(self):
        pass

    def extract_pitch(self, audio_path, time_step=0.01):
        """
        Extracts pitch (F0) using Parselmouth (Praat).
        Returns: (times, f0_values)
        """
        snd = parselmouth.Sound(audio_path)
        pitch = snd.to_pitch(time_step=time_step)
        pitch_values = pitch.selected_array['frequency']
        # Replace 0 (unvoiced) with NaN for easier processing, or keep as 0
        pitch_values[pitch_values == 0] = np.nan
        return pitch.xs(), pitch_values

    def extract_energy(self, y, sr, hop_length=512):
        """
        Extracts RMS energy.
        """
        rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]
        times = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=hop_length)
        return times, rms

    def get_stats(self, pitch_values):
        """
        Returns stats like mean pitch, range, etc.
        """
        valid_pitch = pitch_values[~np.isnan(pitch_values)]
        if len(valid_pitch) == 0:
            return {'mean': 0, 'std': 0, 'min': 0, 'max': 0}
            
        return {
            'mean': np.nanmean(valid_pitch),
            'std': np.nanstd(valid_pitch),
            'min': np.nanmin(valid_pitch),
            'max': np.nanmax(valid_pitch)
        }
