import cv2
if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	print(img.shape)
	x, y = img.shape[0:2]
	img_resize = cv2.resize(img, (int(y / 2),   int(x / 2)))
	cv2.imwrite('figures/2_1.jpg', img_resize)
	print(img_resize.shape)
