import cv2
import numpy as np
import time

url = 0
capture_video = cv2.VideoCapture(url)
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

time.sleep(3) 
count = 0 
background = 0 


for i in range(60):
	return_val , background = capture_video.read()
	if return_val == False :
		continue 

background = np.flip(background, axis=1)


while (capture_video.isOpened()):
	return_val, img = capture_video.read()
	if not return_val :
		break 
	count = count + 1
	img = np.flip(img , axis=1)
	hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

	lower_green = np.array([25, 52, 72])
	upper_green = np.array([102, 255, 255])
	mask1 = cv2.inRange(hsv,lower_green,upper_green)

	lower_green = np.array([25, 189, 118])
	upper_green = np.array([95, 255, 198])
	mask2 = cv2.inRange(hsv,lower_green,upper_green)

	mask1 = mask1+mask2

	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	res1 = cv2.bitwise_and(background,background,mask=mask1)
	res2 = cv2.bitwise_and(img,img,mask=mask2)
	final_output = cv2.addWeighted(res1,1,res2,1,0)
    
    out.write(final_output)
    
	cv2.imshow("INVISIBLE MAN",final_output)
	k = cv2.waitKey(10)
	if k == 27:
		break