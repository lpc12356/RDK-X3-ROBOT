import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	line = cv2.line(img, (50,20), (20,100), (255,0,255), 10)
	cv2.imwrite('figures/3_4.jpg', line)
