#!/usr/bin/python

import sys
import RPi.GPIO as GPIO
from time import time
from time import sleep

GPIO.setmode(GPIO.BCM)

# Ignore warnings
GPIO.setwarnings(False)

class sonic_sensor:                                                                                                                                                            

    def __init__(self, TRIG, ECHO):

        self.TRIG = TRIG #Setup Trigger
        self.ECHO = ECHO #Setup Echo
        
        GPIO.setup(TRIG, GPIO.OUT) #Setup trigger to be output
        GPIO.setup(ECHO, GPIO.IN)  #Setup echo to be input
        print("set-up sonic")

    #def close(self, signal):
    #    GPIO.cleanup()
    #    sys.exit(0)
    #
    #    signal.signal(signal.SIGINT, close)
    #    print("close sonic")
        
    def sonicsensor(self):
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
    print("range check function")
    
    x = int(sensorL.sonicsensor())
    y = int(sensorR.sonicsensor())
    
    sensorLmin = x-12 #define range value for sensors 
    sensorRmin = y-12
    sensorLmax = x+12
    sensorRmax = y+12
    
    if x in range(sensorRmin,sensorRmax) and y in range(sensorLmin,sensorLmax):
        return 0
    elif (x < y):
        return 2
    else:
        return 1
    

sensorL = sonic_sensor(5, 6) #Sensor 1
sensorR = sonic_sensor(18, 19) #Sensor 2

x = sensorL.sonicsensor()
y = sensorR.sonicsensor()
