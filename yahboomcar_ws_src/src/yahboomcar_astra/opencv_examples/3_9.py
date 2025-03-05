import cv2

if __name__ == '__main__':
	img = cv2.imread('figures/yahboom.jpg')
	cv2.putText(img,'This is Yahboom!',(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,200,0),2)
	cv2.imwrite('figures/3_9.jpg', img)
