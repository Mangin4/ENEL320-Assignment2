# ENEL320-Assignment2
<p>Author : Ben Mangin(bma191), Daegan Rose-Love(dnrl17), Oliver Stuitje(ost21), Trent Kamper(tka77)</p>

<h2> Q1 </h2>

![Question 1](/Images/Q1.png)

<h3> a) </h3>
<p>The image below shows the signal and its Fourier transform. The signal is made up of the following functions:
</p>

$$
\begin{align}
x = 30sin(10\pi t)\\
x = 50sin(40\pi t)\\
x = 10sin(60\pi t)
\end{align}
$$


![DFT sample rate of 100](/Images/DFT%20sr=200.png)
<p>The following image shows the same signal, but the Fourier transform only displays one period. This was achieved by using only half of the values obtained from the DFT.</p>

![DFT sample rate of 100](/Images/DFT%20sr=200%20one%20period.png) 

<h3> b) </h3>

![DFT sample rate of 100](/Images/Complexity%20graph%20FFT%20VS%20DFT.png)

<h3> c) </h3>
<p>The plot that we obtain relates to the complexity of the mathematical function. The DFT has a big O complexity of O(N^2), while the FFT has a complexity of O(Nlog(N)). This means that when there are a high number of samples, the FFT will be tractable, whereas the DFT will most likely not be.

Another interesting feature of the DFT is the increasing variability in the time taken. This could be explained by factors not related to the code, such as variability in the speed of a computer.</p>
