import cv2 

img = cv2.imread("Resources/lambo.jpg")
imgResize = cv2.resize(img, (800, 450))
imgCropped = imgResize[100:400, 50:600]
print(img.shape)

cv2.imshow("Image Reesize", imgResize)
cv2.imshow("Image Resize", imgCropped)

cv2.waitKey(0)

