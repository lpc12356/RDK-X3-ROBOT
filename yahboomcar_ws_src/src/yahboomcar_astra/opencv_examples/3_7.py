import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	ellipse = cv2.ellipse(img, (80,80), (20,50),0,0, 360,(255,0,255), 5)
	cv2.imwrite('figures/3_7.jpg', ellipse)
