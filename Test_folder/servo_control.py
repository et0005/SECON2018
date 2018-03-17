import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(05,GPIO.OUT)


class servo:
    def __init__(self,pin):
        self.pin = pin
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)

    def SetAngle(self,angle):
            duty=angle/18+2
            GPIO.output(self.pin,True)
            self.pwm.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(self.pin,False)
            self.pwm.ChangeDutyCycle(0)


claw = servo(05)
rotate = servo(06)
wrist = servo(07)

claw.pwm.stop()
rotate.pwm.stop()
wrist.pwm.stop()
GPIO.cleanup()
