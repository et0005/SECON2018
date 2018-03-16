#import sys
#sys.path.append('/home/pi/Desktop/SECON2018-master/Motor_Test')
import motor_test
from RPi.GPIO import cleanup
from time import sleep

def forward(speed):
    motor_test.motor1.forward(speed)
    motor_test.motor2.forward(speed)
    motor_test.motor3.forward(speed)
    motor_test.motor4.forward(speed)
    print("Moving forward")

def stop():
    motor_test.motor1.stop()
    motor_test.motor2.stop()
    motor_test.motor3.stop()
    motor_test.motor4.stop()
    print("Moving Stop")

def backward(speed):
    motor_test.motor1.backward(speed)
    motor_test.motor2.backward(speed)
    motor_test.motor3.backward(speed)
    motor_test.motor4.backward(speed)
    print("Moving backward")
    
def turnright(speed):   
    motor_test.motor1.forward(speed)
    motor_test.motor2.forward(speed)
    motor_test.motor3.backward(speed)
    motor_test.motor4.backward(speed)
    sleep(1.95)
    stop()
    print("Moving right")
    
def turnleft(speed):
    motor_test.motor1.backward(speed)
    motor_test.motor2.backward(speed)
    motor_test.motor3.forward(speed)
    motor_test.motor4.forward(speed)
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
