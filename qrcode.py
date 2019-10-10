from pyzbar.pyzbar import decode
from PIL import Image


import cv2
import time

# video oject video (with id of camera)
video = cv2.VideoCapture('http://192.168.1.107:5050/video')
a = 0
while True:

  a = a+1
  # frame object
  check, frame = video.read()

  # show the frame
  cv2.imshow("Capturing", frame)


  decode(frame)
  # press any key to out
  key = cv2.waitKey(1)

  if key == ord('q'):
    break

print(a)
# shutdown the camera
video.release()

cv2.destroyAllWindows()
