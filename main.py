#!/usr/bin/env pybricks-micropython
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
MOTOR_MALY_PRAVY = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE, gears=[1, 1])
MOTOR_MALY_LAVY = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=[1, 1])

#senzory
PREDNY_SENZOR =  InfraredSensor(Port.S3)

LAVY_SENZOR = UltrasonicSensor(Port.S1)
PRAVY_SENZOR = UltrasonicSensor(Port.S4)

#variables
opakovanie = 0
x = 0

#konstanty
MAX_SPEED = 100
MID_SPEED = 75
LOW_SPEED = 50


def start(): #start ako S
    global opakovanie
    while opakovanie < 2:
        pohyb.drive(LOW_SPEED, 0)

        while PREDNY_SENZOR.distance() > 40:
            wait(10)

        pohyb.stop()
        wait(500)
        pohyb.turn(55)
        opakovanie += 1

    while opakovanie < 4:
        pohyb.drive(LOW_SPEED, 0)

        while PREDNY_SENZOR.distance() > 40:
            wait(10)

        pohyb.stop()
        wait(500)
        pohyb.turn(-55)
        opakovanie += 1

def stena():
    pohyb.turn(10)
    pohyb.drive(MAX_SPEED, 0)
    wait(3500)
    pohyb.drive(LOW_SPEED, 0)


    while PREDNY_SENZOR.distance() > 40:
        print(PREDNY_SENZOR.distance())

    pohyb.stop()

def napravenie():
    pohyb.straight(-50)
    pohyb.turn(-55)
    pohyb.straight(-15)
    pohyb.straight(50)

def hladanie():
    global opakovanie
    opakovanie = 0
    radlica_opened()
    pohyb.turn(30)
    while opakovanie <= 1:
        if PREDNY_SENZOR.distance() > 40 :
            pohyb.drive(0.5, -100)
        elif PREDNY_SENZOR.distance() <= 40:
            pohyb.drive(LOW_SPEED, 0)
            if PREDNY_SENZOR.distance() <= 10 :
                radlica_closed()
                opakovanie += 1
            else:
                print(PREDNY_SENZOR.distance())
        else:
            print("v riti")       
     
    
    
def radlica_closed():
    MOTOR_MALY_LAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)

def radlica_opened():
    MOTOR_MALY_LAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)


def main():
    start()
    stena()
    napravenie()
    wait(1000)
    hladanie()
    wait(1000)

if __name__ == "__main__":
    main()
