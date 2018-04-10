import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """
        
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 100)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 100)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH)
        print("set-up")

    def forward(self, speed):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(speed)
        print("forward")

           
    def backward(self, speed):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(speed)
        print("backward")

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """

        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)
        

"""
motor1 = Motor(5, 7, 3)
motor2 = Motor(35, 37, 33)
motor3 = Motor(29, 31, 19)
motor4 = Motor(13, 15, 11)
"""
#blue is grnd purple is pwr on board

Passenger = Motor(21, 22, 23) # forward(green), backward(yellow), control(red)
Driver = Motor(13, 16, 17) # forward(green), backward(yellow), control (red)

# This next code is for testing purposes when pins are moved :|
"""
motor1.forward(50)
sleep(3)
motor1.stop()
motor2.forward(50)
sleep(3)
motor2.stop()
motor3.forward(50)
sleep(3)
motor3.stop()
motor4.forward(50)
sleep(3)
motor4.stop()
GPIO.cleanup()
"""
