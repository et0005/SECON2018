#!/usr/bin/python

# ------------------------------------------------
#
#    Title : IR_control.py
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

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Ignore warnings
GPIO.setwarnings(False)

# BOARD labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use GPIO numbering for pins
GPIO.setmode(GPIO.BCM)


class IRsensor:
    def __init__(self, desta, destb, destc):
        self.destA = desta
        self.destB = destb
        self.destC = destc
        print("set-up IR")

# Manually enter route codes for now.
# ( Destination A, Destination B, Destination C)
IR1 = IRsensor(0, 0, 0)
