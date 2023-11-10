import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Generate data
fs = 1000  # sampling freq
T = 1 / fs  # interval
t = np.arange(0, 1, T)  # Time axis

# signal
sig = (signal.square(t, 0.5) + 1) * np.sin(fs * 2 * np.pi * t)

# Fourier data
f = np.fft.fftfreq(len(sig), T)
y = np.fft.fft(sig)
magnitude = np.abs(y)
phase = np.angle(y)

# Mag plot
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.grid(True)
plt.plot(f, magnitude)
plt.title('Magnitude')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

# Phase plot 
plt.subplot(2, 1, 2)
plt.grid(True)
plt.plot(f, phase)
plt.title('Phase')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase')
plt.tight_layout()
plt.show()
