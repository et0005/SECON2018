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
        else:
            return 999

def range_check():
    print("range check function")
    
    x = int(sensor1.sonicsensor())
    y = int(sensor2.sonicsensor())
    
    sensor1min = x-12 #define range value for sensors 
    sensor2min = y-12
    sensor1max = x+12
    sensor2max = y+12
    
    if x in range(sensor2min,sensor2max) and y in range(sensor1min,sensor1max):
        return 0
    elif (x < y):
        return 2
    else:
        return 1
    

sensor1 = sonic_sensor(24, 23) #Sensor 1
sensor2 = sonic_sensor(15, 14) #Sensor 2

x = sensor1.sonicsensor()
y = sensor2.sonicsensor()

print("Sensor 1 is = %d mm" % x)
print("Sensor 2 is = %d mm" % y)

print(range_check())
#sensor1min = x-12 #define range value for sensors 
#sensor2min = y-12 
#sensor1max = x+12
#sensor2max = y+12

# if x in range(sensor2min,sensor2max) and y in range(sensor1min,sensor1max):
#     print "they equal"
# else:
#     print "they not equal"
