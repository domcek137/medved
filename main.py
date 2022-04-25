#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

motor_lavy = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 24])
motor_pravy = Motor(Port.C,  positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 24])
motor_lavy_maly = Motor(Port.D)
motor_pravy_maly = Motor(Port.A)
predny_senzor = InfraredSensor(Port.S2)
lavy_senzor = UltrasonicSensor(Port.S1)
pravy_senzor = UltrasonicSensor(Port.S4)
x = 0

MAX_SPEED = 200
MID_SPEED = 100
LOW_SPEED = 50

while x < 2:
    motor_lavy.run_angle(Low_speed, 90, then = Stop.HOLD)
    motor_pravy.run_angle(Low_speed, 90, then = Stop.HOLD)
    time.sleep(2)
    x += 1

ev3.speaker.beep(1000, 500)



ev3.speaker.beep()