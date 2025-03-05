import cv2
import numpy as np

if __name__ == '__main__':
	dam_img = cv2.imread('figures/4_1_damaged.jpg')
	imgInfo = dam_img.shape
	height = imgInfo[0]
	width = imgInfo[1]
	paint = np.zeros((height,width,1),np.uint8)
	for i in range(50,100):
		paint[i,50] = 255
		paint[i,50+1] = 255
		paint[i,50-1] = 255
	for i in range(100,150):
		paint[150,i] = 255
		paint[150+1,i] = 255
		paint[150-1,i] = 255
	dst_img =  cv2.inpaint(dam_img,paint,3,cv2.INPAINT_TELEA)
	cv2.imwrite("figures/4_1_paint.jpg",paint)
	cv2.imwrite("figures/4_1_result.jpg",dst_img)
