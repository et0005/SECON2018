#!/usr/bin/python

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
from time import time
from time import sleep

# Ignore warnings
GPIO.setwarnings(False)

# BOARD labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use GPIO numbering for pins
GPIO.setmode(GPIO.BCM)


class SonicSensor:
    def __init__(self, TRIG, ECHO):
        self.TRIG = TRIG # Setup Trigger
        self.ECHO = ECHO # Setup Echo
        
        GPIO.setup(TRIG, GPIO.OUT) # Setup trigger to be output
        GPIO.setup(ECHO, GPIO.IN)  # Setup echo to be input

    #   def close(self, signal):
    #   GPIO.cleanup()
    #   sys.exit(0)
    #
    #   signal.signal(signal.SIGINT, close)
    #   print("close sonic")
        
    def sonic_read(self):
        GPIO.output(self.TRIG, False)
        sleep(0.05)
    
        GPIO.output(self.TRIG, True)
        sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            pulse_start = time()

        while GPIO.input(self.ECHO) == 1:
            pulse_end = time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        
        if distance <= 500:
            distance = distance * 10
            return distance
        elif distance > 500:
            return 999


def range_check():
    
    left_value = int(sensorL.sonic_read())
    right_value = int(sensorR.sonic_read())
    
    left_min = left_value - 12  # define range value for sensors
    left_max = left_value + 12

    right_min = right_value - 12
    right_max = right_value + 12
    
    if left_value in range(right_min, right_max) and right_value in range(left_min, left_max):
        return 0
    elif left_value < right_value:
        return 2
    else:  # left_value > right_value
        return 1
    

sensorL = SonicSensor(5, 6)  # Sensor 1
sensorR = SonicSensor(18, 19)  # Sensor 2

x = sensorL.sonic_read()
y = sensorR.sonic_read()
