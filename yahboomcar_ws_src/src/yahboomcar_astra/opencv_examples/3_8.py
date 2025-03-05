import cv2
import numpy as np

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	points = np.array([[120,50], [40,140], [120,70], [110,110], [50,50]], np.int32)
	polylines = cv2.polylines(img, [points],True,(255,0,255), 5)
	cv2.imwrite('figures/3_8.jpg', polylines)
