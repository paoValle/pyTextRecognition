import cv2, time

#video oject video (with id of camera)
video = cv2.VideoCapture(1)
a=0
while True:

  a=a+1
  #frame object
  check, frame = video.read()

  print(check)
  print(frame) #image

  #show the frame
  cv2.imshow("Capturing", frame)

  #press any key to out
  key=cv2.waitKey(1)

  if key==ord('q'):
    break;

print(a)
#shutdown the camera
video.release()

cv2.destroyAllWindows()