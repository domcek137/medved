#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

#velke motory
MOTOR_LAVY = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 24])
MOTOR_PRAVY = Motor(Port.C,  positive_direction=Direction.COUNTERCLOCKWISE, gears=[8, 24])
pohyb = DriveBase(MOTOR_PRAVY, MOTOR_LAVY, wheel_diameter = 45, axle_track = 50)
#male motory
MOTOR_MALY_PRAVY = Motor(Port.D)
MOTOR_MALY_LAVY = Motor(Port.A)

#senzory
PREDNY_SENZOR =  InfraredSensor(Port.S3)

LAVY_SENZOR = UltrasonicSensor(Port.S1)
PRAVY_SENZOR = UltrasonicSensor(Port.S4)

#xxx
x = 0

MAX_SPEED = 200
MID_SPEED = 100
LOW_SPEED = 50

def start(): #start ako S
    while True:
        if (PREDNY_SENZOR.distance()) >= 50:
            pohyb.drive(MID_SPEED, 20)
            print(PREDNY_SENZOR.distance())
        else:
            print(PREDNY_SENZOR.distance())
            pohyb.stop()


def main():
    start()

if __name__ == "__main__":
    main()
