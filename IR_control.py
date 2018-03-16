#!/usr/bin/python

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Ignore warnings
GPIO.setwarnings(False)

# Board labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use board numbering for pins
GPIO.setmode(GPIO.BOARD)


class IRsensor:
    def __init__(self, desta, destb, destc):
        self.destA = desta
        self.destB = destb
        self.destC = destc


IR1 = IRsensor(0, 0, 0)
