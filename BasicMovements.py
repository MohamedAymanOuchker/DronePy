from djitellopy import tello
from time import sleep

tl = tello.Tello()
tl.connect()

tl.takeoff()
tl.send_rc_control(0, 50, 0, 0)

sleep(2)

tl.send_rc_control(0, 0, 0, 30)

sleep(2)

tl.send_rc_control(0, 0, 0, 0)
tl.land()