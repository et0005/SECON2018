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


def stop():
    motor_control.Driver.stop()
    motor_control.Passenger.stop()


def backward(speed):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.backward(speed)
    

def turn_left(speed):
    motor_control.Driver.forward(speed)
    motor_control.Passenger.backward(speed)
    sleep(1.95)
    stop()


def turn_right(speed):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.forward(speed)
    sleep(1.95)
    stop()


def adjust():
    print("Ultrasonic adjustment\n")
    angle = ultrasonic.range_check()
    
    while angle == 1:
        turn_left(62)
        sleep(0.2)
        stop()
        angle = ultrasonic.range_check()
        
    while angle == 2:
        turn_right(62)
        sleep(0.2)
        stop()
        angle = ultrasonic.range_check()
    

def forward_a(InfraredSensor):
    if IR_control.IR1.destA == 0:
        print("Heading to location A. Route indicates turn North (0)\n")
        turn_left(62)
        sleep(1)
        stop()
        sleep(1)

    elif IR_control.IR1.destA == 1:
        print("Heading to location A. Route indicates turn South (1)\n")
        turn_right(62)
        sleep(1)
        stop()
        sleep(1)

    print("Arrived at A. Hitting Button.\n")
    
    adjust()
    
    forward(62)
    sleep(1.4)
    stop()  # simulate button hit time
    sleep(4)  # simulate completion of first objective


def backtrack_a(InfraredSensor):
    print("Backtracking to center.\n")
    
    backward(62)
    sleep(1.4)
    stop()
    sleep(1)

    print("Facing center.\n")

    if IR_control.IR1.destA == 0:  # turn towards plank
        turn_right(62)
        sleep(0.5)
        stop()
        sleep(1)
    elif IR_control.IR1.destA == 1:
        turn_left(62)
        sleep(0.5)
        stop()
        sleep(1)
    
    adjust()


def walk_the_plank():
    print("Walking the plank, arr!")
    
    forward(62)
    sleep(4)
    stop()
    sleep(1)


def forward_b(InfraredSensor):
    if IR_control.IR1.destB == 0:
        print("Heading to location B. Route indicates turn North (0)\n")
        turn_left(62)
        sleep(0.5)
        stop()
        sleep(1)

    elif IR_control.IR1.destB == 1:
        print("Heading to location B. Route indicates turn South (1)\n")
        turn_right(62)
        sleep(0.5)
        stop()
        sleep(1)
        
    print("Arrived at B. Hitting Button.\n")
    
    adjust()
    
    forward(62)
    sleep(1.5)
    stop()
    sleep(1)


def backtrack_b(InfraredSensor):
    print("Backtracking to center.\n")
    
    backward(62)  # return to center
    sleep(1.5)
    stop()
    sleep(1)

    print("Facing center.\n")

    if IR_control.IR1.destB == 0:
        turn_right(62)
        sleep(0.5)
        stop()
        sleep(1)
    elif IR_control.IR1.destB == 1:
        turn_left(62)
        sleep(0.5)
        stop()
        sleep(1)
    
    adjust()


def forward_chest():
    print("Arrived at Treasure Chest.\n")

    forward(62)
    sleep(1.5)
    stop()
    sleep(1)

    print("Pushed Treasure Chest.\n")


def align_to_start():
    print("Facing the ship.\n")

    backward(62)
    sleep(1.5)
    stop()
    sleep(1)

    turn_right(62)
    sleep(0.5)
    stop()
    sleep(1)

    turn_right(62)
    sleep(0.5)
    stop()
    sleep(1)
    
    adjust()


def backtrack_to_start():
    walk_the_plank()


def forward_c(InfraredSensor):
    if IR_control.IR1.destC == 0:
        print("Heading to location C. Route indicates turn North (0)\n")
        turn_left(62)
        sleep(1)
        stop()
        sleep(1)

    elif IR_control.IR1.destC == 1:
        print("Heading to location C. Route indicates turn South (1)\n")
        turn_right(62)
        sleep(1)
        stop()
        sleep(1)
        
    print("Arrived at C. Hitting Button.\n")
    
    adjust()
    
    forward(62)
    sleep(1.4)
    stop()


def complete():
    stop()
    GPIO.cleanup()


def begin(InfraredSensor):
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
