import cv2

vid = cv2.VideoCapture("Resources/Canyon.mp4")

while True:
     success, img = vid.read()
     cv2.imshow("Video", img)
     if cv2.waitKey(1) and 0xFF == ord('q'):
         break