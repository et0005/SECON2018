from sonicTesttest import *
import time
import sys
from RPi.GPIO import cleanup

while True:
        print(sensor2.sonicsensor())
        time.sleep(1)
