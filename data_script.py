import librosa
import numpy as np
import scipy
from scipy.signal import welch

def extract_missing_features(audio_file):
    y, sr = librosa.load(audio_file, sr=None)
    
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=75, fmax=300)
    f0 = f0[~np.isnan(f0)] 
    
    if len(f0) == 0:
        return "Error: No voiced segments detected."
    
    spread1 = np.mean(f0) - np.median(f0)
    spread2 = np.std(f0)
    
    
    ppe = scipy.stats.entropy(np.histogram(f0, bins=10)[0])
    
   
    def detrended_fluctuation_analysis(signal, s=10):
        n = len(signal)
        x = np.cumsum(signal - np.mean(signal))
        
       
        trimmed_length = (n // s) * s  
        reshaped_x = x[:trimmed_length].reshape(-1, s)
        
       
        mean_values = np.mean(reshaped_x, axis=1, keepdims=True)

        rms = np.sqrt(np.mean(np.square(reshaped_x - mean_values)))

        return rms

    dfa = detrended_fluctuation_analysis(y)
    
    def compute_rpde(signal):
        freqs, psd = welch(signal, fs=sr)
        entropy = -np.sum(psd * np.log(psd + 1e-10)) 
        return entropy
    
    rpde = compute_rpde(y)
    
    def correlation_dimension(signal):
        return np.log(np.var(signal) + 1e-10)  
    
    d2 = correlation_dimension(y)
    
    return {
        "Spread1": spread1,
        "Spread2": spread2,
        "PPE": ppe,
        "DFA": dfa,
        "RPDE": rpde,
        "D2": d2
    }

audio_file = "/mnt/d/vit hackathon/sound/untitled.wav"
features = extract_missing_features(audio_file)
print(features)
