import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	cv2.imwrite('figures/3_1.jpg', gray)
