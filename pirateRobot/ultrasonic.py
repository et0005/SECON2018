#!/usr/bin/python

# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
from time import time
from time import sleep

#tolerance = {'A':515 ,'B': 483, 'plank': 2133, 'chest': 965, 'C': 700}
#last_turn = 3

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
        distance = distance * 10
        
        return distance
     

sensorL = SonicSensor(5, 6)  # Sensor 1
sensorR = SonicSensor(20, 19)  # Sensor 2
