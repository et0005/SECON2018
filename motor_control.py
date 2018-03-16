#!/usr/bin/python

# ------------------------------------------------
#
#    Title : motor_control.py
#
#    Authors : Ashley Condrey
#              David Flanigan
#              Nathan Romans
#              Payton Parrott
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
#    sudo python motor_control.py
#
# ------------------------------------------------

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO

# Ignore warnings
GPIO.setwarnings(False)

# Board labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use board numbering for pins
GPIO.setmode(GPIO.BOARD)


class Motor:
    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """
        # Initialize pins
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl

        # Setup pins as output
        GPIO.setup(self.pinForward, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pinBackward, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pinControl, GPIO.OUT, initial=GPIO.LOW)

        # Configure PWM on output pins, pin enable and duty cycle
        # GPIO.PWM(output channel , frequency of PWM signal)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)

        # Start at 0% duty cycle
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)

        GPIO.output(self.pinControl,GPIO.HIGH)

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_forward.ChangeDutyCycle(speed)
        self.pwm_backward.ChangeDutyCycle(0)

    def backward(self, speed):
        """ pinBackward is the backward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)


# Create motors and assign pins. (pinForward, pinBackward, pinControl)

# motor1 = Motor(5, 7, 3)
# motor2 = Motor(35, 37, 33)
# motor3 = Motor(29, 31, 19)
# motor4 = Motor(13, 15, 11)

motor3 = Motor(5, 7, 3)
motor2 = Motor(35, 37, 33)
motor4 = Motor(29, 31, 19)
motor1 = Motor(13, 15, 11)

GPIO.cleanup()
