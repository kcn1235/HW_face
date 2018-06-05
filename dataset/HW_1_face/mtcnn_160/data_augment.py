from PIL import Image
import skimage
from skimage import data, exposure, img_as_float
import os
import numpy as np
from PIL import Image  
from PIL import ImageEnhance
import cv2

dirname = os.path.dirname(os.path.abspath(__file__))

def GaussieNoisy(image,sigma):
    row,col,ch = image.shape
    mean = 0
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy.astype(np.uint8)

def GaussieNoisyGrey(image,sigma):
    row,col = image.shape
    mean = 0
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = image + gauss
    return noisy.astype(np.uint8)

for i in range(2000):
	im = Image.open(dirname + '/%d/%d_1.jpg' % (i,i))
	im_gam1 = im.point(lambda p: p * 2)
	im_gam2 = im.point(lambda p: p * 0.5)
	im_Contrast = ImageEnhance.Contrast(im)
	im_Contrast = im_Contrast.enhance(1.5)
	im_sharp = ImageEnhance.Sharpness(im)
	im_sharp = im_sharp.enhance(3)
	im_noise = np.array(im)
	if im_noise.ndim == 2:
		im_noise = GaussieNoisyGrey(im_noise,0.2)
	else:
		im_noise = GaussieNoisy(im_noise,0.2)
	im_noise = Image.fromarray(im_noise)
	im_gam1.save(dirname + '/%d/%d_2.jpg' % (i,i))
	im_gam2.save(dirname + '/%d/%d_3.jpg' % (i,i))
	im_Contrast.save(dirname + '/%d/%d_4.jpg' % (i,i))
	im_sharp.save(dirname + '/%d/%d_5.jpg' % (i,i))
	im_noise.save(dirname + '/%d/%d_6.jpg' % (i,i))


	im_transpose = im.transpose(Image.FLIP_LEFT_RIGHT)
	im_gam1 = im_transpose.point(lambda p: p * 2)
	im_gam2 = im_transpose.point(lambda p: p * 0.5)
	im_Contrast = ImageEnhance.Contrast(im_transpose)
	im_Contrast = im_Contrast.enhance(1.5)
	im_sharp = ImageEnhance.Sharpness(im_transpose)
	im_sharp = im_sharp.enhance(3)
	im_noise = np.array(im_transpose)
	if im_noise.ndim == 2:
		im_noise = GaussieNoisyGrey(im_noise,0.2)
	else:
		im_noise = GaussieNoisy(im_noise,0.2)
	im_noise = Image.fromarray(im_noise)
	im_transpose.save(dirname + '/%d/%d_7.jpg' % (i,i))
	im_gam1.save(dirname + '/%d/%d_8.jpg' % (i,i))
	im_gam2.save(dirname + '/%d/%d_9.jpg' % (i,i))
	im_Contrast.save(dirname + '/%d/%d_10.jpg' % (i,i))
	im_sharp.save(dirname + '/%d/%d_11.jpg' % (i,i))
	im_noise.save(dirname + '/%d/%d_12.jpg' % (i,i))
	#print(i)
