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

<h3>Q2</h3>

![Question 2](/Images/Q2.png)

<h3> a) </h3>

<h3> b) </h3>

<h3> c) </h3>

<h3> d) </h3>

<h2> Q3 </h2>

<h3> Image before deblurring </h3>

![Question 3 - image before deblurring](/Images/Q3.png)

<h3> Image after deblurring </h3>

![Image after deblurring](/Images/Deblurred-image.png)

<p> to deblur the image a weiner filter was used. To calibrate the LEN and THETA variables of the PSF, an iterative approach was applied. a variable i was declared, each iteration to deblur the image would start with LEN = 20 (arbitruarily chosen) then create an image, plot it, then add 1 to i.
After each iteration, i would be added to the current value of LEN. Using this technique, the different images could be observed and whichever was chosen to give the highest quality was used for further calibration. This same system was used to calibrate THETA, and the noise factor of the image.
The final values were found to be as follows: LEN = 46.3, THETA = 20, noise factor = 0.01


