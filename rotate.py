from PIL import Image  
import os

dirname = os.path.dirname(os.path.abspath(__file__))

for i in range(2000):
	im = Image.open(dirname + '/%d/%d_1.jpg' % (i,i))  
	im_rotate = im.rotate(90)
	im_rotate.save(dirname + '/%d/%d_2.jpg' % (i,i))
	im_rotate = im.rotate(180)
	im_rotate.save(dirname + '/%d/%d_3.jpg' % (i,i))
	im_rotate = im.rotate(270)
	im_rotate.save(dirname + '/%d/%d_4.jpg' % (i,i))