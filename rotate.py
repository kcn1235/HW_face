from PIL import Image  
import os

for i in range(2000):
	im = Image.open('/%d/%d_1.jpg' % i, % i)  
	im_rotate = im.rotate(90)
	im_rotate.save('d:/%d_2.jpg')
	im_rotate = im.rotate(180)
	im_rotate.save('d:/%d_3.jpg')
	im_rotate = im.rotate(270)
	im_rotate.save('d:/%d_4.jpg')