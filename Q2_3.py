import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate data
fs = 1000  # sampling freq
T = 1 / fs  # interval
t = np.arange(0, 1, T)  # time axis

# signal
sig = (signal.square(t, 0.5) + 1) * np.sin(fs * 2 * np.pi * t)

# plot spectrogram
plt.specgram(sig, Fs=fs, cmap='viridis', NFFT=256, noverlap=128)
plt.title('Spectrogram of Doppler Wave')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Intensity (dB)')
plt.show()
