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

# Dependent Files
from pirateRobot import routeEngine
from pirateRobot import IR_control

# Turn on rPI
# Read IR for alignment
#    Display on 7seg for alignment
# Wait for 1, 2, 3, GO
#    Flip Switch
#         Upon switch
#              Read IR route
#              Load IR route into class variables (for turns only)
#              IR route gets plugged into route engine
#         Execute route via route engine

if IR_control.IR1.destA == 1:
    if IR_control.IR1.destB == 1:
        if IR_control.IR1.destC == 1:
            print("Wait for start signal\n")

else:
    print("Begin Route!\n")
    print("Route is : ABC : ")
    print(IR_control.IR1.destA)
    print(IR_control.IR1.destB)
    print(IR_control.IR1.destC)
    print("\n")
        
    routeEngine.begin(IR_control.IR1)
  