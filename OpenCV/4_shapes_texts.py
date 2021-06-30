import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# print(img.shape)
# img[:] = 255, 0 , 0


cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 5)
cv2.arrowedLine(img, (0,210),(img.shape[1],210),(255,255,100),5)
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), 5) # cv2.Filled or -1 
cv2.circle(img, (300, 300), 80, (0, 0, 255), 5) 
cv2.putText(img, "HELLO",(250,100), cv2.FONT_HERSHEY_COMPLEX, 2, (100, 100 ,100),2 ,cv2.LINE_AA)



cv2.imshow("Image", img)
cv2.waitKey(0)