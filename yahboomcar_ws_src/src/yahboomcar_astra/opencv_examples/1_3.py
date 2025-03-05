import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	(b,g,r) = img[100,100]
	print(b,g,r)
	for i in range(0,10):
		for j in range(0,200):
			img[i,j] = (0,0,0)
	cv2.imwrite("figures/1_3.jpg",img)
		