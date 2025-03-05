import cv2
import numpy as np

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	imgInfo = img.shape
	height = imgInfo[0]
	width = imgInfo[1]
	deep = imgInfo[2]
	newImgInfo = (height*2,width,deep)
	dst = np.zeros(newImgInfo,np.uint8)#uint8
	for i in range(0,height):
		for j in range(0,width):
			dst[i,j] = img[i,j]
			dst[height*2-i-1,j] = img[i,j]
	cv2.imwrite('figures/2_4.jpg', dst)
