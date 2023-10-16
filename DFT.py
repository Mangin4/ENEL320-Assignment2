import numpy as np
import matplotlib.pyplot as plt
import time

#function for the DFT
def DFT(x):
    N = len(x)          #samples
    n = np.arange(N)    #range for sumation
    k = n.reshape((N, 1))
    e = np.exp((-2j*np.pi*k*n)/N)
    return np.dot(x, e)

def FFT(x):
    return np.fft.fft(x)

def complexity(x):
    X = [] 
    XFFT = []
    y = np.arange(1,2000,1)

    for i in range(1,2000):
        seconds = time.perf_counter()
        sr = i
        ts = 1/sr
        t = np.arange(0,1,ts)
        x = 30*np.sin(2*np.pi*5*t)
        x += 50*np.sin(2*np.pi*20*t)
        x += 10*np.sin(2*np.pi*30*t)
        R = DFT(x)
        last = time.perf_counter()
        X.append(last - seconds)
    
    for i in range(1,2000):
        seconds = time.perf_counter()
        sr = i
        ts = 1/sr
        t = np.arange(0,1,ts)
        x = 30*np.sin(2*np.pi*5*t)
        x += 50*np.sin(2*np.pi*20*t)
        x += 10*np.sin(2*np.pi*30*t)
        R = np.fft.fft(x)
        last = time.perf_counter()
        XFFT.append(last - seconds)

    plt.plot(y, X, 'r', label = "DFT")
    plt.plot(y, XFFT, 'b', label = "FFT")
    plt.xlabel("Sample Rate (samples)")
    plt.ylabel("Time Taken (s)")
    plt.title("Plot of time taken for FFT and DFT")
    plt.legend()
    plt.show()





def plot():
    sr = 200
    ts = 1/sr
    t = np.arange(0,1,ts)

    x = 30*np.sin(2*np.pi*5*t)
    x += 50*np.sin(2*np.pi*20*t)
    x += 10*np.sin(2*np.pi*30*t)

    X = DFT(x)

    N = len(X)
    n = np.arange(N)
    T = N/sr
    freq = n/T

    oneP = N//2
    fOneP = freq[:oneP]
    XoneP = X[:oneP]

    plt.subplot(2,1,1)
    plt.plot(t,x)
    plt.ylabel("Amplitude")
    plt.title("Singal")

    plt.subplot(2,1,2)
    plt.stem(freq, abs(X) ,markerfmt=" ", basefmt="-b")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude |X(freq)|")
    plt.title("Fourier Transform")
    plt.show()

plot()