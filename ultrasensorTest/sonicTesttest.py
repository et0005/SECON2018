import RPi.GPIO as GPIO
import time
import signal
import sys

class U_sensor:

        def __init__(self,pinTrigger,pinEcho):
                # use Raspberry Pi board pin numbers
                GPIO.setmode(GPIO.BOARD)

                # set GPIO Pins
                self.pinTrigger=pinTrigger
                self.pinEcho=pinEcho
                # set GPIO input and output channels
                GPIO.setup(self.pinTrigger, GPIO.OUT)
                GPIO.setup(self.pinEcho, GPIO.IN)
                
        def close(self,signal, frame):
                print("\nTurning off ultrasonic distance detection...\n")
                GPIO.cleanup() 
                sys.exit(0)

                signal.signal(signal.SIGINT, close)


                

        def sonicsensor(self):
                while True:
                        # set Trigger to HIGH
                        GPIO.output(self.pinTrigger, True)
                        # set Trigger after 0.01ms to LOW
                        time.sleep(0.00001)
                        GPIO.output(self.pinTrigger, False)

                        startTime = time.time()
                        stopTime = time.time()

                        # save start time
                        while 0 == GPIO.input(self.pinEcho):
                                startTime = time.time()

                        # save time of arrival
                        while 1 == GPIO.input(self.pinEcho):
                                stopTime = time.time()

                        # time difference between start and arrival
                        TimeElapsed = stopTime - startTime
                        # multiply with the sonic speed (34300 cm/s)
                        # and divide by 2, because there and back
                        distance = (TimeElapsed * 34300) / 2

                        if distance <= 300:
                            return distance

                        
                        time.sleep(.05)

sensor1=U_sensor(12,18) #trigger then echo
sensor2=U_sensor(7, 11)
