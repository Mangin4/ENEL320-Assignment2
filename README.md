# ENEL320-Assignment2
<p>Author : Ben Mangin(bma191), Daegan Rose-Love(dnrl17)</p>

<h2> Q1 </h2>

![Question 1](/Images/Q1.png)

<h3> a) </h3>
<p>The image below shows the signal and its fourier transform. The siganl is made up of the following functions. 

        x = 30*sin(2*np.pi*5*t)
        x = 50*sin(2*np.pi*20*t)
        x = 10*sin(2*np.pi*30*t)</p>


![DFT sample rate of 100](/Images/DFT%20sr=200.png)
<p>The following image shows the same signal but the fourier transform only shows one period of. This was done by only useing half of the values that come out of the DFT </p>

![DFT sample rate of 100](/Images/DFT%20sr=200%20one%20period.png) 

<h3> b) </h3>

![DFT sample rate of 100](/Images/Complexity%20graph%20FFT%20VS%20DFT.png)

<h3> c) </h3>
<p>The plot that we get relates to the complexity of the mathfunction. DFT has a big o commplexity of O(N^2) and the FFT has a complexity of O(Nlog(N)). This means when there is a high number of samples the FFT will be Tractable where as the DFT will most likly not be. 

Anohter interesting feature in the DFT is there is a increasing variablility in the time taken. this could be explained factors not relating to the code like variablility in the speed of a computer.</p>
