import RPi.GPIO as GPIO
import time
import signal
import sys

class U_sensor2:
        # use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BOARD)

        # set GPIO Pins
        pinTrigger = 7
        pinEcho = 11

        def close(signal, frame):
                print("\nTurning off ultrasonic distance detection...\n")
                GPIO.cleanup() 
                sys.exit(0)

        signal.signal(signal.SIGINT, close)

        # set GPIO input and output channels
        GPIO.setup(pinTrigger, GPIO.OUT)
        GPIO.setup(pinEcho, GPIO.IN)

        def sonicsensor():
                while True:
                        # set Trigger to HIGH
                        GPIO.output(pinTrigger, True)
                        # set Trigger after 0.01ms to LOW
                        time.sleep(0.00001)
                        GPIO.output(pinTrigger, False)

                        startTime = time.time()
                        stopTime = time.time()

                        # save start time
                        while 0 == GPIO.input(pinEcho):
                                startTime = time.time()

                        # save time of arrival
                        while 1 == GPIO.input(pinEcho):
                                stopTime = time.time()

                        # time difference between start and arrival
                        TimeElapsed = stopTime - startTime
                        # multiply with the sonic speed (34300 cm/s)
                        # and divide by 2, because there and back
                        distance = (TimeElapsed * 34300) / 2

                        if distance <= 300:
                            return distance

                        
                        time.sleep(.05)

        while True:
                print("%.1f" % sonicsensor())
                time.sleep(.05)
