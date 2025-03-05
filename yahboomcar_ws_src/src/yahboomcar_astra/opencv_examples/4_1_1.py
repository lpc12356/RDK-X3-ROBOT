import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	for i in range(50,100):
		img[i,50] =   (0,0,0)
		img[i,50+1] =   (0,0,0)
		img[i,50-1] =   (0,0,0)
	for i in range(100,150):
		img[150,i] =   (0,0,0)
		img[150,i+1] =   (0,0,0)
		img[150-1,i] =   (0,0,0)
	cv2.imwrite('figures/4_1_damaged.jpg',img)
