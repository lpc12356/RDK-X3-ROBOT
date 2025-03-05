import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	rect = cv2.rectangle(img, (50,20), (100,100), (255,0,255), 10)
	cv2.imwrite('figures/3_5.jpg', rect)
