I = im2double(imread('blur_car.png'));
%imshow(I);
title('Original Image (courtesy of MIT)');


%remove gaussian noise
PSF = fspecial('gaussian',7,10);
V = .0001;
WT = zeros(size(I));
WT(5:end-4,5:end-4) = 1;
INITPSF = ones(size(PSF));
[J, P] = deconvblind(I,INITPSF,20,10*sqrt(V),WT);





%blurred = imfilter(I, PSF, 'conv', 'circular');
%figure, imshow(blurred)

%noise_mean = 0;
noise_var = 0.008;
estimated_nsr_J = noise_var / var(J(:));
LEN = 47;
THETA = 20;
i = 0;
PSF_motion = fspecial('motion', LEN, THETA);
wnr1 = deconvwnr(J, P, estimated_nsr_J);
wnr3 = deconvwnr(wnr1, PSF_motion, 0.095);
imshow(wnr3)

%disp(LEN)
