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

# Ignore warnings
GPIO.setwarnings(False)

# BOARD labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use GPIO numbering for pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN)

while(1):
    enable = GPIO.input(24)
    
    if(enable):
        IR_control.IR1.ir_read()
        
        print("Begin Route!\n")
        print("Route is : ABC : ")
        print(IR_control.IR1.A)
        print(IR_control.IR1.B)
        print(IR_control.IR1.C)
        print("\n")

        #routeEngine.begin(IR_control.IR1)

    else:
        print("Huh")
