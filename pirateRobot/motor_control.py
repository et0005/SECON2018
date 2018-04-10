#!/usr/bin/python

# ------------------------------------------------
#
#    Title : motor_control.py
#
#    Authors : Ashley Condrey
#              David Flanigan
#              Nathan Romans
#              Payton Parrott
#              Elena Todorovska
#
#    Created On : 01/01/2018
#
#    Description : This program performs basic
#    motor driver demonstration, such as: turns
#    both left and right, tight turns, forward
#    rotation and backward rotation.
#
#    Notes : This will be run on a Raspberry Pi
#    using a 12V battery and 4 DC Motors. The
#    motors are driven with PWM using a L293D.
#
#    Run Instructions : Type the following:
#    ./motor_control.py
#
# ------------------------------------------------

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
from time import sleep
# Ignore warnings
GPIO.setwarnings(False)

# BOARD labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use GPIO numbering for pins
GPIO.setmode(GPIO.BCM)

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """

        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH) 

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)    

    def backward(self, speed):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

# WIRING NOTES : Color coding is as follows :
# Power = Purple
# GND = Blue
# Control = Red
# Forward = Green
# Backward = Yellow
# WARNING: AA Battery pack Power is Blue and GND is Black :WARNING


# Create motors and assign pins. (pinForward, pinBackward, pinControl)
Passenger = Motor(21, 22, 23)
Driver = Motor(13, 16, 17) 


# Outdated, 2 chips and 4 motors
# rearPassenger = Motor(5, 7, 3)
# frontPassenger = Motor(35, 37, 33)
# frontDriver = Motor(29, 31, 19)
# rearDriver = Motor(13, 15, 11)
