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

![Real World Signal](/Images/Model_of_Pulse_Doppler_Radar_Waveform.png)

<p> </p>


<h3> b) </h3>

![Doppler Mag and Phase](/Images/Doppler_Mag_and_Phase.png)

<h3> c) </h3>

![Doppler Spectrogram](/Images/Doppler_specgram.png)

<h3> d) </h3>

<h2> Q3 </h2>

<h3> Image before deblurring </h3>

![Question 3 - image before deblurring](/Images/Q3.png)

<p> 
As this image has some motion blur, a Wiener filter was thought to be applied to attempt to 'deblur' the image. A Wiener filter depends on a specificed vector length (LEN), angle (THETA) and NSR (Noise to Signal Ratio). Using an arbitrary guess and check method, the image was plotted for a range of these variables until a number plate could be assertained. Two different images were arrived at that could be cross compared to assertain a number plate reading.
</p>

<h3> Wiener Point Spread Function </h3>

![Point Spread Function (Kernel Matrix) of filter](/Images/Matrix.PNG)

<p>
While this is not necessarilly an optimized and efficient process (as well as some ambiguity within the output) it is sufficient to deduce that the number plate of the car is "N449 JJ8". This deblurred image could be used in conjunction with other tools such as carjam to deduce the history of the vehicle, criminal investigation units also possess much more sofisticated databases to retrieve more information about the car.
</p>

<h3> Images after deblurring with Wiener Kernel </h3>

![Image after deblurring](/Images/Deblurred-image.png)

![Image after Deblurring: T=19, L=42, NSR=0.005](/deblur_car_2.PNG)
