import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	circle = cv2.circle(img, (80,80), 50, (255,0,255), 10)
	cv2.imwrite('figures/3_6.jpg', circle)
