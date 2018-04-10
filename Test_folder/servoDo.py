# Module for Raspberry Pi GPIO pins
import RPi.GPIO as GPIO
from time import sleep

# Ignore warnings
GPIO.setwarnings(False)

# BOARD labels are printed on the board: PIN[#]
# BCM labels are functional labels     : GPIO[#]
# Use GPIO numbering for pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(05,GPIO.OUT)

# pwm=GPIO.PWM(05,50)
# pwm.start(0)


class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)

    def set_angle(self, angle):
            duty = angle/18+2
            GPIO.output(self.pin, True)
            self.pwm.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(self.pin, False)
            self.pwm.ChangeDutyCycle(0)

            # OLD CODE:
            # duty = angle / 18 + 2
            # GPIO.output(05, True)
            # pwm.ChangeDutyCycle(duty)
            # sleep(1)
            # GPIO.output(05, False)
            # pwm.ChangeDutyCycle(0)


claw = Servo(05)
rotate = Servo(06)
wrist = Servo(07)

wrist.set_angle(0)
wrist.set_angle(30)
wrist.set_angle(60)
wrist.set_angle(90)
wrist.set_angle(120)
wrist.set_angle(150)
wrist.set_angle(180)


claw.pwm.stop()
rotate.pwm.stop()
wrist.pwm.stop()
GPIO.cleanup()
