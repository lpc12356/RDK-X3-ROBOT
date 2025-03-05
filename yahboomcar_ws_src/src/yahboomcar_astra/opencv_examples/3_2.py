import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, binary = cv2.threshold(gray,180,255,cv2.THRESH_BINARY_INV) 
	cv2.imwrite('figures/3_2.jpg', binary)
