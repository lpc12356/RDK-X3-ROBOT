import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	imgG = cv2.GaussianBlur(gray,(3,3),0)
	dst = cv2.Canny(imgG,50,50)
	cv2.imwrite('figures/3_3.jpg', dst)
