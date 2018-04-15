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
#from pirateRobot import servo_control

global tolerance_max
global tolerance_min
global last_turn

tolerance_max = {'A':550 ,'B': 580, 'plank': 205, 'chest': 965, 'C': 700}
tolerance_min = {'A':450 ,'B': 300, 'plank': 0, 'chest': 865, 'C': 600}
#plank long distance: 2133
#b old distance 483, 383
last_turn = 3

# Functions to move DC motors in specific way to accomplish movement in each direction.
def forward(speed):
    motor_control.Driver.forward(speed)
    motor_control.Passenger.forward(speed)


def stop():
    motor_control.Driver.stop()
    motor_control.Passenger.stop()


def backward(speed):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.backward(speed)
    

def turn_right(speed, turns):
    motor_control.Driver.forward(speed)
    motor_control.Passenger.backward(speed)
    sleep(turns)
    stop()


def turn_left(speed, turns):
    motor_control.Driver.backward(speed)
    motor_control.Passenger.forward(speed)
    sleep(turns)
    stop()


# Functions to move servos in specific way to accomplish movement.
#def straighten():
#    servo_control.wrist.SetAngle(90)


#def approach_wheel():
#    servo_control.rotate.SetAngle(0)
#    servo_control.claw.SetAngle(180)


#def turn_wheel():
#    servo_control.claw.SetAngle(0)
#    servo_control.rotate.SetAngle(270)
#    servo_control.claw.SetAngle(180)


# Functions to make adjustments using ultrasonic sensors.
def range_check(tolerance_max, tolerance_min):
    
    left_value = int(ultrasonic.sensorL.sonic_read())
    right_value = int(ultrasonic.sensorR.sonic_read())
    
    if left_value >= tolerance_max or right_value >= tolerance_max or left_value <= tolerance_min or right_value <= tolerance_min:
        # totally out of range
        return 3
    else:
        left_min = left_value - 4  # define range value for sensors
        left_max = left_value + 4

        right_min = right_value - 4
        right_max = right_value + 4
        
        if left_value in range(right_min, right_max) and right_value in range(left_min, left_max):
            # equal values, exit
            return 2
        elif left_value < right_value:
            # too far to the left, turn right
            return 0
        else:
            #otherwise too far to the right, turn left
            return 1
        
        
def adjust(tolerance_max, tolerance_min):
    
    print("Ultrasonic adjustment\n")
    angle = range_check(tolerance_max, tolerance_min)
    
    while angle == 0: # too far to the right, turn left
        print("Too far to the left, TURN right")
        #turn_right(75, 0.2)
        turn_right(75, 0.1)
        sleep(0.1)
        stop()
        angle = range_check(tolerance_max, tolerance_min)
         
    while angle == 1: # too far to the left, turn right
        print("Too far to the right, TURN left")
        #turn_left(75, 0.2)
        turn_left(75, 0.1)
        sleep(0.1)
        stop()
        angle = range_check(tolerance_max, tolerance_min)

    # While angle == 2: equal do nothing

    while angle == 3: # totally out of range
        print("totally out of range")
        if last_turn == 1:
            print("Turn Left")
            #turn_right(75, 0.2)
            turn_left(75,0.1)
            sleep(0.1)
            stop()
            angle = range_check(tolerance_max, tolerance_min)
        elif last_turn == 0:
            print("Turn Right")
            turn_right(75,0.1)
            #turn_left(75,0.2)
            sleep(0.1)
            stop()
            angle = range_check(tolerance_max, tolerance_min)
        else:    
            print("ELSE")

# Functions for each segment of a route.
def forward_a(InfraredSensor):
    if IR_control.IR1.destA == 0:
        print("Heading to location A. Route indicates turn North (0)\n")
        turn_right(75, 1.7)
        global last_turn
        last_turn = 0 #keep track of last turn
        stop()
        sleep(1)

    elif IR_control.IR1.destA == 1:
        print("Heading to location A. Route indicates turn South (1)\n")
        turn_left(75, 1.7)
        global last_turn
        last_turn = 1 #keep track of last turn
        stop()
        sleep(1)

    print("Arrived at A. Hitting Button.\n")
    
    #adjust(tolerance_max['A'], tolerance_min['A'])
    
    #forward(62)
    backward(62)
    sleep(1.8)
    stop()  # simulate button hit time
    sleep(4)  # simulate completion of first objective


def backtrack_a(InfraredSensor):
    print("Backtracking to center.\n")
    
    #backward(62)
    forward(62)
    sleep(1.8)
    stop()
    sleep(1)

    print("Facing center.\n")

    if IR_control.IR1.destA == 0:  # turn towards plank
        turn_right(75, 1.5)#1.6)
        global last_turn
        last_turn = 0 #keep track of last turn
        stop()
        sleep(1)
    elif IR_control.IR1.destA == 1:
        turn_left(75, 1.5)#1.6)
        global last_turn
        last_turn = 1 #keep track of last turn
        stop()
        sleep(1)
    
    adjust(tolerance_max['plank'], tolerance_min['plank'])


def walk_the_plank():
    print("Walking the plank, arr!")
    
    #forward(62)
    backward(62)
    sleep(3.4)
    stop()
    sleep(1)


def forward_b(InfraredSensor):
    if IR_control.IR1.destB == 0:
        print("Heading to location B. Route indicates turn North (0)\n")
        turn_right(75, 1.7)
        global last_turn
        last_turn = 0 #keep track of last turn
        stop()
        sleep(1)

    elif IR_control.IR1.destB == 1:
        print("Heading to location B. Route indicates turn South (1)\n")
        turn_left(75, 1.7)
        global last_turn
        last_turn = 1 #keep track of last turn
        stop()
        sleep(1)
        
    print("Arrived at B. Hitting Button.\n")
    
    adjust(tolerance_max['B'], tolerance_min['B'])
    
    forward(62)
    #backward(62)
    sleep(1.6)
    stop()
    sleep(1)


def backtrack_b(InfraredSensor):
    print("Backtracking to center.\n")
    
    backward(62)  # return to center
    #forward(62)
    sleep(1.6)
    stop()
    sleep(1)

    print("Facing chest.\n")

    if IR_control.IR1.destB == 0:
        turn_right(75, 1.3)
        global last_turn
        last_turn = 0 #keep track of last turn
        stop()
        sleep(1)
    elif IR_control.IR1.destB == 1:
        turn_left(75, 1.3)
        global last_turn
        last_turn = 1 #keep track of last turn
        stop()
        sleep(1)
    
    adjust(tolerance_max['chest'], tolerance_min['chest'])


def forward_chest():
    print("Arrived at Treasure Chest.\n")

    forward(80)
    sleep(1.5)
    stop()
    sleep(1)

    print("Pushed Treasure Chest.\n")


def align_to_start():
    print("Facing the ship.\n")

    backward(80)
    sleep(1.5)
    stop()
    sleep(1)

    '''turn_left(75, 1.5)
    stop()
    sleep(1)

    turn_left(75, 1.5)
    stop()
    sleep(1)
    
    global last_turn
    last_turn = 1 #keep track of last turn
    
    adjust(tolerance_max['C'], tolerance_min['C'])'''


def backtrack_to_start():
    walk_the_plank()


def forward_c(InfraredSensor):
    if IR_control.IR1.destC == 0:
        print("Heading to location C. Route indicates turn North (0)\n")
        #turn_right(75, 1.2)
        turn_left(75, 1.2)
        global last_turn
        last_turn = 1#keep track of last turn
        stop()
        sleep(1)

    elif IR_control.IR1.destC == 1:
        print("Heading to location C. Route indicates turn South (1)\n")
        #turn_left(75, 1.2)
        turn_right(75, 1.2)
        global last_turn
        last_turn = 0 #keep track of last turn
        stop()
        sleep(1)
        
    print("Arrived at C. Hitting Button.\n")
    
    #adjust(tolerance_max['A'], tolerance_min['A'])
    
    #forward(62)
    backward(62)
    sleep(1.6)
    stop()


# Functions at most basic level, start and end round.
def complete():
    stop()
    GPIO.cleanup()


def begin(InfraredSensor):
    forward_a(IR_control.IR1.destA)
    backtrack_a(IR_control.IR1.destA)
    walk_the_plank()
    forward_b(IR_control.IR1.destB)
    backtrack_b(IR_control.IR1.destB)
    '''
    forward_chest()
    align_to_start()
    backtrack_to_start()
    forward_c(IR_control.IR1.destC)'''
    complete()

