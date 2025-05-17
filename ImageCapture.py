from djitellopy import tello
import cv2

tl = tello.Tello()
tl.connect()
print(tl.get_battery())
tl.streamon()

while True:
    img = tl.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)