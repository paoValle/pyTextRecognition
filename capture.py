import cv2
import time

# video oject video (with id of camera)
video = cv2.VideoCapture('http://192.168.1.107:5050/video')
a = 0
while True:

  a = a+1
  # frame object
  check, frame = video.read()

  # Threshold to obtain binary image
  thresh = cv2.threshold(frame, 220, 255, cv2.THRESH_BINARY_INV)[1]

  # Create custom kernel
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
  # Perform closing (dilation followed by erosion)
  close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

  # Invert image to use for Tesseract
  result = 255 - close

  # show the frame
  cv2.imshow("Capturing", result)

  # press any key to out
  key = cv2.waitKey(1)

  if key == ord('q'):
      break

print(a)
# shutdown the camera
video.release()

cv2.destroyAllWindows()
