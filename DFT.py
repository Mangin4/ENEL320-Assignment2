import numpy as np
import matplotlib.pyplot as plt

sr = 100
ts = 1/sr
t = np.arange(0,1,ts)

x = 3*np.sin(2*np.pi*10*t)
x += 5*np.sin(2*np.pi*7*t)
x += np.sin(2*np.pi*3*t)

def DFT(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp((-2j*np.pi*k*n)/N)
    return np.dot(x, e)

X = DFT(x)

N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T

oneP = N//2
fOneP = freq[:oneP]

XoneP = X[:oneP]

plt.stem(fOneP, abs(XoneP),markerfmt=" ", basefmt="-b")
plt.xlim(0, 15)
plt.tight_layout()
plt.show()