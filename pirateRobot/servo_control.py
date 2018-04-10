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
GPIO.setup(06,GPIO.OUT)
GPIO.setup(07,GPIO.OUT)

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

claw.pwm.stop()
rotate.pwm.stop()
wrist.pwm.stop()
GPIO.cleanup()
