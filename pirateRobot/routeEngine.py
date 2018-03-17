#!/usr/bin/python

# ------------------------------------------------
#
#    Title : routeEngine.py
#
#    Authors : Ashley Condrey
#              David Flanigan
#              Nathan Romans
#              Payton Parrott
#              Elena Todorovska
#
#    Created On : 01/01/2018
#
#    Description : This program performs 
#
#    Notes : This will be run on a Raspberry Pi
#    using a 12V battery and 4 DC Motors. The
#    motors are driven with PWM using a L293D.
#
# ------------------------------------------------

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
from time import sleep
# Dependent Files
from pirateRobot import motor_control
from pirateRobot import IR_control
from pirateRobot import ultrasonic

# Functions to move motors in specific way to accomplish movement in each direction.
def forward(speed):
    motor_control.Driver.forward(speed)
    motor_control.Passenger.forward(speed)
    print("Forward")


def stop():
    motor_control.Driver.stop()
    motor_control.Passenger.stop()
    print("Stop")


def backward(speed):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.backward(speed)
    print("Backward")
    

def turnleft(speed):
    motor_control.Driver.forward(speed)
    motor_control.Passenger.backward(speed)
    print("Turn Left")
    sleep(1.95)
    stop()


def turnright(speed):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.forward(speed)
    print("Turn Right")
    sleep(1.95)
    stop()


def adjust():
    print("Ultrasonic adjustment\n")
    x = ultrasonic.range_check()
    print(x)
    

def forward_a(IRsensor):
    if IR_control.IR1.destA == 0:
        print("Heading to location A. Route indicates turn North (0)\n")
        turnleft(55)
        sleep(1)
        stop()
        sleep(1)

    elif IR_control.IR1.destA == 1:
        print("Heading to location A. Route indicates turn South (1)\n")
        turnright(55)
        sleep(1)
        stop()
        sleep(1)

    print("Arrived at A. Hitting Button.\n")
    
    forward(55)
    sleep(1.4)
    stop()  # simulate button hit time
    sleep(4)  # simulate completion of first objective


def backtrack_a(IRsensor):
    print("Backtracking to center.\n")
    
    backward(55)
    sleep(1.4)
    stop()
    sleep(1)

    print("Facing center.\n")

    if IR_control.IR1.destA == 0:  # turn towards plank
        turnright(55)
        sleep(0.5)
        stop()
        sleep(1)
    elif IR_control.IR1.destA == 1:
        turnleft(55)
        sleep(0.5)
        stop()
        sleep(1)


def walk_the_plank():
    print("Walking the plank, arr!")
    
    forward(55)
    sleep(4)
    stop()
    sleep(1)


def forward_b(IRsensor):
    if IR_control.IR1.destB == 0:
        print("Heading to location B. Route indicates turn North (0)\n")
        turnleft(55)
        sleep(0.5)
        stop()
        sleep(1)

    elif IR_control.IR1.destB == 1:
        print("Heading to location B. Route indicates turn South (1)\n")
        turnright(55)
        sleep(0.5)
        stop()
        sleep(1)
        
    print("Arrived at B. Hitting Button.\n")

    forward(55)
    sleep(1.5)
    stop()
    sleep(1)


def backtrack_b(IRsensor):
    print("Backtracking to center.\n")
    
    backward(55)  # return to center
    sleep(1.5)
    stop()
    sleep(1)

    print("Facing center.\n")

    if IR_control.IR1.destB == 0:
        turnright(55)
        sleep(0.5)
        stop()
        sleep(1)
    elif IR_control.IR1.destB == 1:
        turnleft(55)
        sleep(0.5)
        stop()
        sleep(1)


def forward_chest():
    print("Arrived at Treasure Chest.\n")

    forward(55)
    sleep(1.5)
    stop()
    sleep(1)

    print("Pushed Treasure Chest.\n")


def align_to_start():
    print("Facing the ship.\n")

    backward(55)
    sleep(1.5)
    stop()
    sleep(1)
    
    turnright(55)
    sleep(0.5)
    stop()
    sleep(1)
    
    turnright(55)
    sleep(0.5)
    stop()
    sleep(1)


def backtrack_to_start():
    walk_the_plank()


def forward_c(IRsensor):
    if IR_control.IR1.destC == 0:
        print("Heading to location C. Route indicates turn North (0)\n")
        turnleft(55)
        sleep(1)
        stop()
        sleep(1)

    elif IR_control.IR1.destC == 1:
        print("Heading to location C. Route indicates turn South (1)\n")
        turnright(55)
        sleep(1)
        stop()
        sleep(1)
        
    print("Arrived at C. Hitting Button.\n")
    
    forward(55)
    sleep(1.4)
    stop()


def complete():
    stop()
    GPIO.cleanup()


def begin(IRsensor):
    forward_a(IR_control.IR1.destA)
    backtrack_a(IR_control.IR1.destA)
    walk_the_plank()
    forward_b(IR_control.IR1.destB)
    backtrack_b(IR_control.IR1.destB)
    forward_chest()
    align_to_start()
    backtrack_to_start()
    forward_c(IR_control.IR1.destC)
    complete()
