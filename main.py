#!/usr/bin/env pybricks-micropython
import operator
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
MOTOR_MALY_PRAVY = Motor(Port.D, positive_direction=Direction.COUNTERCLOCKWISE, gears=[1, 1])
MOTOR_MALY_LAVY = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE, gears=[1, 1])

#senzory
PREDNY_SENZOR =  InfraredSensor(Port.S3)

#STOP_TLACITKO = TouchSensor(Port.S2)

LAVY_SENZOR = UltrasonicSensor(Port.S1)
PRAVY_SENZOR = UltrasonicSensor(Port.S4)

#stopwatch
cas = StopWatch()
cas2 = StopWatch()
cas3 = StopWatch()
cas4 = StopWatch()

#variables
strnast = 0
opakovanie = 0
koniec = 0
x = 0
zemiak = 0

#konstanty
MAX_SPEED = 100
MID_SPEED = 75
LOW_SPEED = 50


def start(): #start ako S
    print("start")
    global opakovanie
    while opakovanie < 2:
        pohyb.drive(LOW_SPEED, 0)
        while PREDNY_SENZOR.distance() > 30:
            wait(10)
    
        pohyb.stop()
        wait(500)
        pohyb.turn(50)
        opakovanie += 1

    while opakovanie < 4:
        pohyb.drive(LOW_SPEED, 0)

        while PREDNY_SENZOR.distance() > 30:
            wait(10)

        pohyb.stop()
        wait(500)
        pohyb.turn(-55)
        opakovanie += 1

def stena():
    print("stena")
    pohyb.turn(5)
    pohyb.drive(MAX_SPEED, 2)
    wait(3500)
    pohyb.drive(LOW_SPEED, 2)


    while PREDNY_SENZOR.distance() > 30:
        wait(10)

    pohyb.stop()

def napravenie():
    print("napravenie")
    pohyb.straight(-50)
    pohyb.turn(-55)
    cas.reset()
    while cas.time() < 2000 :
        pohyb.drive(-20, 0)
    pohyb.stop()     
    pohyb.straight(45)

def hladanie_jadro():
    print("hladanie_jadro")
    radlica_opened()
    pohyb.turn(45)
    pohyb.reset()
    global zemiak
    global strnast 
    global koniec
    koniec = 0
    while pohyb.angle() >= -90 and koniec == 0:
        if PREDNY_SENZOR.distance() > 40 :
            wait(10)
            pohyb.drive(1, -50)
        elif PREDNY_SENZOR.distance() <= 40:
            wait(10)
            while PREDNY_SENZOR.distance() <= 40:
                wait(10)
                zemiak = pohyb.angle()
                print(zemiak)
                pohyb.drive(LOW_SPEED, 0)
                if PREDNY_SENZOR.distance() <= 10 :
                    wait(10)
                    pohyb.drive(LOW_SPEED, 0)
                    wait(500)
                    radlica_closed()
                    koniec += 1
                    break
                else:
                    print(PREDNY_SENZOR.distance())
        else:
            print("v riti") 
    strnast += 1
    hladanie()


def hladanie():
    print("hladanie")
    global strnast
    global koniec
    print(strnast)
    if strnast == 0:
        hladanie_jadro()
    elif strnast == 1 and koniec == 0:
        pohyb.turn(45)
        pohyb.straight(40)
        hladanie_jadro()

def kde_domov_muj():
    print("kde domov muj")
    global opakovanie
    global zemiak
    opakovanie = 0
    zemiak = (zemiak + 45) * (-1)
    pohyb.turn(zemiak)
    pohyb.drive(-MAX_SPEED,  0)
    wait(4000)
    pohyb.stop()
    pohyb.straight(15)
    pohyb.turn(-55)

def jazda_stena(relate):
    print("jazda stena")
    global opakovanie
    while relate(PRAVY_SENZOR.distance() , 300):
        wait(10)
        print(PRAVY_SENZOR.distance()) 
        if LAVY_SENZOR.distance() < 100:
            wait(10)
            pohyb.drive(LOW_SPEED, 25)
        elif LAVY_SENZOR.distance() == 100:
            wait(10)
            pohyb.drive(LOW_SPEED, 0)
        else:
            pohyb.drive(LOW_SPEED, -25) 
    opakovanie += 1
    pri_stene()

    
def pri_stene():
    print("pri stene")
    global opakovanie
    if opakovanie == 0:
        jazda_stena(operator.gt)
    elif opakovanie == 1:
        jazda_stena(operator.lt)
    else:
        pohyb.stop()
        print("malo by to fungovat")

def inverted_S():
    print("inverted S")
    global cas2
    x = 0
    while x == 0 :
        if PRAVY_SENZOR.distance() > 250 :
            pohyb.straight(40)
            pohyb.turn(50)
            pohyb.drive(-LOW_SPEED,  0)
            
            wait(1000)
            pohyb.stop()
            pohyb.straight(75)
            x += 1

    pohyb.turn(60)
    pohyb.drive(-LOW_SPEED,  0)
    
    wait(1000)
    pohyb.stop()
    pohyb.straight(120)

    pohyb.turn(-50)
    pohyb.drive(-LOW_SPEED,  0)
    
    wait(1000)
    pohyb.stop()
    pohyb.straight(70)

    pohyb.turn(-55)
    pohyb.drive(-LOW_SPEED,  0)
    wait(1000)
    pohyb.stop()
    pohyb.drive(MAX_SPEED, 5)

    wait(5000)










    #         wait(10)
    #         pohyb.drive(MID_SPEED, 52 )
    #         print(PRAVY_SENZOR.distance())
    #     elif PRAVY_SENZOR.distance() < 250:
    #         wait(10)
    #         print(PRAVY_SENZOR.distance())
    #         pohyb.drive(MID_SPEED, -5)
    #         if LAVY_SENZOR.distance() > 400:
    #             wait(10)
    #             print(PRAVY_SENZOR.distance())
    #             cas2.reset()
    #             x = 1
    #             print("mejbi hotovo")
    # while x == 1:
    #     if PRAVY_SENZOR.distance() < 100 and cas2.time() > 1000:
    #         wait(10)
    #         pohyb.drive(MAX_SPEED, 0)
    #     else:
    #         pohyb.drive(MID_SPEED, -52)
        
        
        
    
def radlica_closed():
    print("radlica closed")
    MOTOR_MALY_LAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)

def radlica_opened():
    print("radlica")
    MOTOR_MALY_LAVY.run_target(1000, 80, then=Stop.HOLD, wait=False)
    MOTOR_MALY_PRAVY.run_target(1000, -80, then=Stop.HOLD, wait=False)


def main():
    start()
    stena()
    napravenie()
    wait(1000)
    hladanie()
    kde_domov_muj() 
    pri_stene()
    inverted_S()


if __name__ == "__main__":
    main()
    

#toto pisal dominik + adam <3