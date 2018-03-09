import sys
sys.path.append('/home/pi/Motor_Test/')
import motor_test
from RPi.GPIO import cleanup
from time import sleep

def forward(speed):
    motor_test.motor1.forward(speed)
    motor_test.motor2.forward(speed)
    motor_test.motor3.forward(speed)
    motor_test.motor4.forward(speed)

def stop():
    motor_test.motor1.stop()
    motor_test.motor2.stop()
    motor_test.motor3.stop()
    motor_test.motor4.stop()

def backward(speed):
    motor_test.motor1.backward(speed)
    motor_test.motor2.backward(speed)
    motor_test.motor3.backward(speed)
    motor_test.motor4.backward(speed)
    
def turnleft(speed):   
    motor_test.motor1.backward(speed)
    motor_test.motor2.backward(speed)
    motor_test.motor3.forward(speed)
    motor_test.motor4.forward(speed)
    sleep(2.20)
    stop()
    
def turnright(speed):
    motor_test.motor1.forward(speed)
    motor_test.motor2.forward(speed)
    motor_test.motor3.backward(speed)
    motor_test.motor4.backward(speed)
    sleep(2.20)
    stop()
    
#main
"""turnleft(60)
sleep(3)
turnright(60)
stop()
cleanup()
"""
