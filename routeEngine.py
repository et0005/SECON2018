#!/usr/bin/python

#
#            _______________________________________
#           |                 WHEEL                 |                  E
#           |                                       |                  |
#           |                                       |               N--+--S
#           |                                       |                  |
#           |                                       |                  W
#           |                                       |
#           |                                       |
#           |                TREASURE               |
#           |                  ___                  |
#           |                 |   |                 |
#           |                 |___|                 |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |    ||                           ||    |
#           |    ||  B                     B  ||    |
#           |    ||                           ||    |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |             ________                  |
#           |             \       \                 |
#           |              \  RAMP \                |
#           |_______________\       \_______________|
#           |                _______                |
#           |               |       |               |
#        C  | A             | START |             A |  C
#           |               |_______|               |
#           |_______________________________________|
#
#
#           IR Input at START:      North (0)   South (1)
#
#              MSB   --------------   LSB       Bin.     Route        Route
#    bit        4      3       2       1        #        #
#
#               1      1       1       1        15       N/A          WAIT
#               0      0       0       0        0        1            A : Left, B: Left, C: Left
#               0      0       0       1        1        2            A : Left, B: Left, C: Right
#               0      0       1       0        2        3            A : Left, B: Right, C: Left
#               0      0       1       1        3        4            A : Left, B: Right, C: Right
#               0      1       0       0        4        5            A : Right, B: Left, C: Left
#               0      1       0       1        5        6            A : Right, B: Left, C: Right
#               0      1       1       0        6        7            A : Right, B: Right, C: Left
#               0      1       1       1        7        8            A : Right, B: Right, C: Right
#
#    func.    Start    A       B       C             (Bin. + 1)
#

import RPi.GPIO as GPIO
import motor_control.py
from time import sleep


# Functions to move motors in specific way to accomplish movement in each direction.
def forward(speed):
    motor_control.motor1.forward(speed)
    motor_control.motor2.forward(speed)
    motor_control.motor3.forward(speed)
    motor_control.motor4.forward(speed)


def stop():
    motor_control.motor1.stop()
    motor_control.motor2.stop()
    motor_control.motor3.stop()
    motor_control.motor4.stop()


def backward(speed):
    motor_control.motor1.backward(speed)
    motor_control.motor2.backward(speed)
    motor_control.motor3.backward(speed)
    motor_control.motor4.backward(speed)


def turnleft(speed):
    motor_control.motor1.backward(speed)
    motor_control.motor2.backward(speed)
    motor_control.motor3.forward(speed)
    motor_control.motor4.forward(speed)
    sleep(2.20)
    stop()


def turnright(speed):
    motor_control.motor1.forward(speed)
    motor_control.motor2.forward(speed)
    motor_control.motor3.backward(speed)
    motor_control.motor4.backward(speed)
    sleep(2.20)
    stop()


def turn4route(IR[]):
    if IR[2] == 0:
        turnleft(47)
    elif IR[2] == 1:
        turnright(47)

def forward_a():

        print("Heading to location A. Route indicates turn North (0)\n")


        print("Heading to location A. Route indicates turn South (1)\n")

    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    print("Arrived at A. Hitting Button.\n")
    sleep(1.4)
    stop()  # simulate button hit time
    sleep(4)  # simulate completion of first objective


def backtrack_a():
    backward(50)  # return to center
    print("Backtracking to center.\n")
    sleep(1.4)
    stop()
    sleep(1)
    print("Facing center.\n")
    if IR[2] == 0: # turn towards plank
        turnright(47)
    elif IR[2] == 1:
        turnleft(47)


def walk_the_plank():
    sleep(0.5)
    stop()
    sleep(1)
    forward(50)


def forward_b():
    if IR[1] == 0:
        turnleft(47)
        print("Heading to location B. Route indicates turn North (0)\n")

    elif IR[1] == 1:
        turnright(47)
        print("Heading to location B. Route indicates turn South (1)\n")

    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    print("Arrived at B. Hitting Button.\n")
    sleep(1.4)
    stop()  # simulate button hit time
    sleep(1)  # simulate completion of first objective


def backtrack_b():
    backward(50)  # return to center
    print("Backtracking to center.\n")
    sleep(1.4)
    stop()
    sleep(1)
    print("Facing center.\n")
    if IR[1] == 0:
        turnright(47)
    elif IR[1] == 1:
        turnleft(47)


def forward_chest():
    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    print("Arrived at Treasure Chest.\n")
    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    print("Pushed Treasure Chest.\n")


def align_to_start():
    print("Facing the ship.\n")
    turnright(47)
    turnright(47)


def backtrack_to_start():
    forward(50)
    forward(50)
    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    sleep(5.4)  # cross the plank back up to complete C
    stop()
    sleep(1)


def forward_c():
    if IR[0] == 0:
        turnleft(47)
        print("Heading to location C. Route indicates turn North (0)\n")

    elif IR[0] == 1:
        turnright(47)
        print("Heading to location C. Route indicates turn South (1)\n")

    sleep(0.5)
    stop()
    sleep(1)
    forward(50)
    print("Arrived at C. Hitting Button.\n")
    sleep(1.4)
    stop()  # simulate button hit time
    sleep(1)  # simulate completion of first objective


def complete():
    stop()
    GPIO.cleanup()


def begin():
    forward_a()
    backtrack_a()
    walk_the_plank()
    forward_b()
    backtrack_b()
    forward_chest()
    align_to_start()
    backtrack_to_start()
    forward_c()
    complete()

