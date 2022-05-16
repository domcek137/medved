#!/usr/bin/env pybricks-micropython
import operator
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

def kde_domov_muj():
    pohyb.drive(-MAX_SPEED,  0)
    wait(3500)
    pohyb.stop()
    pohyb.straight(15)
    pohyb.turn(-55)

def jazda_stena(relate):
    global opakovanie
    #r_hodnota_senzora = PRAVY_SENZOR.distance()
    while relate(PRAVY_SENZOR.distance() , 200): 
        print(PRAVY_SENZOR.distance())       #r_hodnota_senzora
        if LAVY_SENZOR.distance() < 100:
            #print("pravy {r_h_s}".format(r_h_s = r_hodnota_senzora))
            pohyb.drive(LOW_SPEED, 25)
        elif LAVY_SENZOR.distance() == 100:
            pohyb.drive(LOW_SPEED, 0)
        else:
            pohyb.drive(LOW_SPEED, -25)
            #p_hodnota_senzora = PRAVY_SENZOR.distance()
            #print("lavy {p_h_s}".format(p_h_s = p_hodnota_senzora)) 
    opakovanie += 1
    pri_stene()

    
                        

def pri_stene():
    global opakovanie
    if opakovanie == 0:
        jazda_stena(operator.gt)
    elif opakovanie == 1:
        jazda_stena(operator.lt)
    else:
        print("malo by to fungovat")
    
def radlica_closed():
    MOTOR_MALY_LAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)

def radlica_opened():
    MOTOR_MALY_LAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)


def main():
    '''
    start()
    stena()
    napravenie()
    wait(1000)
    hladanie()
    wait(1000)
    kde_domov_muj()
    '''
    pri_stene()

if __name__ == "__main__":
    main()


#toto pisal dominik 