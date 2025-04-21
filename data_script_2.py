import numpy as np
import librosa
import pyrem as prqa  # For RPDE
import nolds  # For DFA and D2
import parselmouth  # For jitter, shimmer, and HNR

def extract_features(audio_file, sr=44100, trim_silence=True):
    """
    Extract voice features from an Audacity-recorded WAV file.
    
    Parameters:
    - audio_file (str): Path to the WAV file.
    - sr (int): Sampling rate (default 44100 Hz, common in Audacity).
    - trim_silence (bool): Whether to trim silence from the audio (default True).
    
    Returns:
    - dict: Extracted features or error message if no voiced segments detected.
    """
    # Load audio file with specified sampling rate
    y, sr = librosa.load(audio_file, sr=sr, mono=True)

    # Preprocessing: Trim silence (optional) and normalize
    if trim_silence:
        y, _ = librosa.effects.trim(y, top_db=20)  # Remove silence below 20 dB
    y = y - np.mean(y)  # Remove DC offset
    y = y / np.max(np.abs(y))  # Normalize to [-1, 1]

    # Extract fundamental frequency (F0)
    f0, voiced_flag, _ = librosa.pyin(
        y,
        fmin=50,  # Broad range for human voices
        fmax=500,
        sr=sr,
        frame_length=2048,  # Good balance for 44.1kHz
        hop_length=256,  # Finer hop for Audacity's high-res recordings
        resolution=0.01
    )
    f0 = f0[voiced_flag]  # Keep only voiced frames
    f0 = f0[~np.isnan(f0)]  # Remove NaN values

    if len(f0) < 10:
        return "Error: Insufficient voiced segments detected. Try speaking louder or closer to the mic."

    # **1. Compute RPDE**
    try:
        rpde = prqa.rpde(f0, tau=1, dim=3)
    except Exception:
        rpde = np.nan

    # **2. Compute DFA**
    try:
        dfa = nolds.dfa(y[librosa.effects.preemphasis(y) > 0], min_n=4, max_n=1000)
    except Exception:
        dfa = np.nan

    # **3. Compute Correlation Dimension (D2)**
    try:
        d2 = nolds.corr_dim(y, emb_dim=10)
    except Exception:
        d2 = np.nan

    # **4. Extract Jitter, Shimmer, and HNR using Praat**
    sound = parselmouth.Sound(audio_file)
    pitch = sound.to_pitch(time_step=0.005, pitch_floor=50, pitch_ceiling=500)
    point_process = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")
    
    jitter = parselmouth.praat.call(
        [sound, point_process], 
        "Get jitter (local)", 
        0, 0, 0.0001, 0.02, 1.3
    )
    shimmer = parselmouth.praat.call(
        [sound, point_process], 
        "Get shimmer (local)", 
        0, 0, 0.0001, 0.02, 1.3
    )
    hnr = parselmouth.praat.call(
        sound, 
        "To Harmonicity (cc)", 
        0.01, 75, 0.1, 1.0
    ).values.mean()

    # Return features
    return {
        "RPDE": float(rpde) if not np.isnan(rpde) else None,
        "DFA": float(dfa) if not np.isnan(dfa) else None,
        "D2": float(d2) if not np.isnan(d2) else None,
        "Jitter": float(jitter) if jitter is not None else None,
        "Shimmer": float(shimmer) if shimmer is not None else None,
        "HNR": float(hnr) if not np.isnan(hnr) else None
    }

# Example Usage
if __name__ == "__main__":
    audio_file = "/mnt/d/vit hackathon/sound/untitled.wav"  # Replace with your file path
    features = extract_features(audio_file)
    print(features)