#import sys
#sys.path.append('/home/pi/Desktop/SECON2018-master/Motor_Test')
import motor_test
from RPi.GPIO import cleanup
from time import sleep

def forward(speed):
    motor_test.Driver.forward(speed)
    motor_test.Passenger.forward(speed)
    print("Moving forward")

def stop():
    motor_test.Driver.stop()
    motor_test.Passenger.stop()
    print("Moving Stop")

def backward(speed):
    motor_test.Driver.backward(speed)
    motor_test.Passenger.backward(speed)
    print("Moving backward")
    
def turnright(speed):   
    motor_test.Driver.forward(speed)
    motor_test.Passenger.backward(speed)
    sleep(1.95)
    stop()
    print("Moving right")
    
def turnleft(speed):
    motor_test.Driver.backward(speed)
    motor_test.Passenger.forward(speed)
    sleep(1.95)
    stop()
    print("Moving left")
    
#main
"""turnleft(60)
sleep(3)
turnright(60)
stop()
cleanup()
"""
