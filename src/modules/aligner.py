import whisper
import torch
import warnings

# Suppress FP16 warning on CPU
warnings.filterwarnings("ignore")

class AudioAligner:
    def __init__(self, model_size="base"):
        print(f"Loading Whisper model ({model_size})...")
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = whisper.load_model(model_size, device=device)
        print("Whisper model loaded.")

    def transcribe(self, audio_path):
        """
        Transcribes audio and returns segments with word-level timestamps.
        Note: Standard Whisper doesn't output word-level timestamps by default in all versions,
        but we can use the 'word_timestamps' option if available or approximate from segments.
        For Antigravity, we ideally need word-level.
        """
        # Transcribe with word timestamps
        result = self.model.transcribe(audio_path, word_timestamps=True)
        return result

if __name__ == "__main__":
    # Test stub
    aligner = AudioAligner()
    # print(aligner.transcribe("test.mp3"))
