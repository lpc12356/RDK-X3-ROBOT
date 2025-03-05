import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	dst = img[0:100,100:200]
	cv2.imwrite('figures/2_2.jpg', dst)
