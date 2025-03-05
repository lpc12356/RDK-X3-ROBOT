import cv2

if __name__ == '__main__':
	frame = cv2.VideoCapture(8)
	if frame.isOpened():
		ret,img = frame.read()
		cv2.imwrite('figures/1_2.jpg',img)
	frame.release()
