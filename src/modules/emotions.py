from dataclasses import dataclass

@dataclass
class EmotionPreset:
    name: str
    pitch_shift: float = 0.0      # Semitones
    pitch_variance: float = 1.0   # Multiplier for F0 dynamic range
    speed_factor: float = 1.0     # Global speed multiplier
    pause_prob: float = 0.0       # Probability of pause at punctuation
    breath_prob: float = 0.0      # Probability of breath
    volume_dynamics: float = 1.0  # Multiplier for volume range

PRESETS = {
    'calm': EmotionPreset(
        name='calm',
        pitch_shift=-1.0, 
        pitch_variance=0.8,
        speed_factor=0.9,
        pause_prob=0.3,
        breath_prob=0.2
    ),
    'excited': EmotionPreset(
        name='excited',
        pitch_shift=2.0,
        pitch_variance=1.5,
        speed_factor=1.1,
        volume_dynamics=1.3,
        breath_prob=0.4
    ),
    'suspense': EmotionPreset(
        name='suspense',
        pitch_shift=-2.0,
        pitch_variance=0.6,
        speed_factor=0.85,
        pause_prob=0.6,
        breath_prob=0.5
    ),
     'sad': EmotionPreset(
        name='sad',
        pitch_shift=-1.5,
        pitch_variance=0.5,
        speed_factor=0.8,
        pause_prob=0.5,
        breath_prob=0.3
    ),
     'confident': EmotionPreset(
        name='confident',
        pitch_shift=-0.5,
        pitch_variance=1.1,
        speed_factor=1.0,
        pause_prob=0.2,
        breath_prob=0.1
    ),
      'storytelling': EmotionPreset(
        name='storytelling',
        pitch_shift=0.0,
        pitch_variance=1.3,
        speed_factor=1.0,
        pause_prob=0.4,
        breath_prob=0.3
    )
}

def get_preset(name: str) -> EmotionPreset:
    return PRESETS.get(name.lower(), PRESETS['calm'])
