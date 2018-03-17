import RPi.GPIO as GPIO
import time
from time import sleep
GPIO.setmode(GPIO.BOARD)

class sonic_sensor:

    def __init__(self, TRIG, ECHO):

        self.TRIG = TRIG #Setup Trigger
        self.ECHO = ECHO #Setup Echo
        
        GPIO.setup(TRIG, GPIO.OUT) #Setup trigger to be output
        GPIO.setup(ECHO, GPIO.IN)  #Setup echo to be input

    def close(self, signal):
        GPIO.cleanup()
        sys.exit(0)

        signal.signal(signal.SIGINT, close)
        
    def sonicsensor(self):
        
        GPIO.output(self.TRIG, False)
        time.sleep(.05)
    
        GPIO.output(self.TRIG, True)
        time.sleep(0.00001)
        GPIO.output(self.TRIG, False)

        while GPIO.input(self.ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(self.ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        if distance <= 500:
            distance = distance * 10
            return distance

def range_check():
        
    x = int(sensor1.sonicsensor())
    y = int(sensor2.sonicsensor())
    sensor1min = x-12 #define range value for sensors 
    sensor2min = y-12
    sensor1max = x+12
    sensor2max = y+12
    if x in range(sensor2min,sensor2max) and y in range(sensor1min,sensor1max):
        return 0  #equal
    elif (x < y):
        return 2 #turnright
    else:
        return 1 #turnleft
    
#main()
sensor1 = sonic_sensor(12, 16) #Sensor 1
sensor2 = sonic_sensor(11, 13) #Sensor 2
"""
x = int(sensor1.sonicsensor())
y = int(sensor2.sonicsensor())

print("Sensor 1 is = %d mm" % x)
print("Sensor 2 is = %d mm" % y)
"""
#print(range_check())
#sensor1min = x-12 #define range value for sensors 
#sensor2min = y-12 
#sensor1max = x+12
#sensor2max = y+12
"""
if x in range(sensor2min,sensor2max) and y in range(sensor1min,sensor1max):
    print "they equal"
else:
    print "they not equal"
"""
