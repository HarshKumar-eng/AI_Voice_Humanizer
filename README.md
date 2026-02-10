# Antigravity - Voice Humanizer

Antigravity uses AI and signal processing to inject human emotion into robotic TTS voices.

## Prerequisites

1.  **Python 3.10+**
2.  **FFmpeg** must be installed and added to your system PATH.
    *   Windows: `winget install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org/).

## Installation

```bash
pip install -r requirements.txt
```

## Running the Web UI

1.  Start the Flask server:
    ```bash
    python app.py
    ```
2.  Open your browser to: `http://127.0.0.1:5000`
3.  Upload a `.wav` or `.mp3` file (e.g., a flat AI voice recording).
4.  Select an emotion (e.g., "Excited", "Sad").
5.  Wait for processing (files are saved to `outputs/`).

## How it Works

*   **Logic**: The system uses `parselmouth` (Praat) to modify the pitch contour and `librosa` (via `pydub` wrapper in future iterations, currently direct manipulation) to adjust speed based on selected emotion presets.
*   **Presets**: Defined in `src/modules/emotions.py`. You can tweak pitch/speed values there.

## Troubleshooting

*   **Error: "ffmpeg not found"**: Ensure FFmpeg is installed and in your PATH.
*   **Error: "snd object"**: Issues with `parselmouth` loading the audio. Ensure it's a valid WAV/MP3.
