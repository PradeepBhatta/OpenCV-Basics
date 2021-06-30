import cv2 
import numpy as np

img = cv2.imread("Resources/lambo.jpg")
imgResize = cv2.resize(img, (400, 225))

hor = np.hstack((imgResize, imgResize))
ver = np.vstack((imgResize, imgResize))

cv2.imshow("Horizontal Image", hor)
cv2.imshow("Vertical Image", ver)
cv2.waitKey(0)
