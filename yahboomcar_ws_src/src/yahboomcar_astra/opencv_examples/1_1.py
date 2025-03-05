import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	cv2.imwrite("figures/1_1.jpg",img)	#新建文件yahboom_new.jpg，并且把yahboom.jpg写进去
