import cv2
import datetime

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
date = str(datetime.datetime.now())

cam.set(3, 640)
cam.set(4, 480)
cam.set(10, 200)
while(cam.isOpened()):
    ret, img = cam.read()
    if ret == True:
        out.write(img)
        cv2.putText(img, date, (100, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2 )
        cv2.imshow("Capture", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
out.release()
cv2.destroyAllWindows()