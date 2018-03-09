# Servo Control
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(05,GPIO.OUT)

pwm=GPIO.PWM(05,50)
pwm.start(0)


def SetAngle(angle):
        duty=angle/18+2
        GPIO.output(05,True)
        pwm.ChangeDutyCycle(duty)
        sleep(1)
        GPIO.output(05,False)
        pwm.ChangeDutyCycle(0)

SetAngle(0)
SetAngle(20)
SetAngle(40)
SetAngle(60)
SetAngle(80)
SetAngle(100)
SetAngle(120)
SetAngle(140)
SetAngle(160)
SetAngle(180)
SetAngle(100)
SetAngle(60)
SetAngle(20)

pwm.stop()
GPIO.cleanup()

