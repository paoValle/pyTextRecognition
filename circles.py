# import the necessary packages
import numpy as np
import cv2

import cv2
import time

# video oject video (with id of camera)
video = cv2.VideoCapture(0)
a = 0
while True:

  a = a+1
  # frame object
  check, image = video.read()

  output = image.copy()
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # detect circles in the image
  circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 200, circles=2)

  try:
    # ensure at least some circles were found
    if circles is not None:
      # convert the (x, y) coordinates and radius of the circles to integers
      circles = np.round(circles[0, :]).astype("int")

      # loop over the (x, y) coordinates and radius of the circles
      for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
  except:
    print("no data")
  # show the output image
  cv2.imshow("grey", gray)
  cv2.imshow("output", output)
  key=cv2.waitKey(1)

  if key == ord('q'):
      break

print(a)
# shutdown the camera
video.release()

cv2.destroyAllWindows()