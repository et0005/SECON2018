#!/usr/bin/python

# ------------------------------------------------
#
#    Title : main.py
#
#    Authors : Ashley Condrey
#              David Flanigan
#              Nathan Romans
#              Payton Parrott
#              Elena Todorovska
#
#    Created On : 01/01/2018
#
#    Description : This program is the main driver. 
#
#    Notes : This will be run on a Raspberry Pi
#    using a 12V battery and 4 DC Motors. The
#    motors are driven with PWM using a L293D.
#
# ------------------------------------------------

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Dependent Files
from pirateRobot import routeEngine
from pirateRobot import IR_control
import serial

try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except:
    ser = serial.Serial('/dev/ttyACM1', 9600)

while 1 :
    coordinates = ser.readline()
    print coordinates
    if (coordinates[0] == '1'):
        IR_control.IR1.A = 0
        IR_control.IR1.B = 0
        IR_control.IR1.C = 0
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '2'):
        IR_control.IR1.A = 0
        IR_control.IR1.B = 0
        IR_control.IR1.C = 1
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '3'):
        IR_control.IR1.A = 0
        IR_control.IR1.B = 1
        IR_control.IR1.C = 0
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '4'):
        IR_control.IR1.A = 0
        IR_control.IR1.B = 1
        IR_control.IR1.C = 1
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '5'):
        IR_control.IR1.A = 1
        IR_control.IR1.B = 0
        IR_control.IR1.C = 0
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '6'):
        IR_control.IR1.A = 1
        IR_control.IR1.B = 0
        IR_control.IR1.C = 1
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '7'):
        IR_control.IR1.A = 1
        IR_control.IR1.B = 1
        IR_control.IR1.C = 0
        routeEngine.begin(IR_control.IR1)
    elif (coordinates[0] == '8'):
        IR_control.IR1.A = 1
        IR_control.IR1.B = 1
        IR_control.IR1.C = 1
        routeEngine.begin(IR_control.IR1)
    else:
        pass
