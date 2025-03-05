import cv2
import numpy as np

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	imgInfo = img.shape
	height = imgInfo[0]
	width = imgInfo[1]
	matShift = np.float32([[1,0,100],[0,1,50]]) # 2*3
	dst = cv2.warpAffine(img, matShift, (width,height))
	cv2.imwrite('figures/2_3.jpg', dst)
