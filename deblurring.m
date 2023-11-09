

% Deblur Car Image. 

% Import Image of Car (Blury)
image = im2double(imread('blur_car.png'));

% Weiner Deconvolution set up
LEN = 42;
THETA = 19;
point_spread_function = fspecial('motion', LEN, THETA);

% Estimate SNR
noise_var = 0.005;
estimated_nsr = noise_var / var(image(:));

% Apply Weiner 
output_wnr = deconvwnr(image,point_spread_function,estimated_nsr);

% Print Image 
imshow(output_wnr)




