import sys
sys.path.append('/home/pi/Navigation')
import Navigation
from RPi.GPIO import cleanup
from time import sleep

#main
"""
Navigation.turnleft(60)
sleep(3)
Navigation.turnright(60)
"""
"""
Remember turn functions have built in sleep
around (2) seconds to complete a turn
"""
#Route 010
Navigation.turnleft(47) #turn toward objective A0
sleep(0.5)
Navigation.stop()
sleep(1)
Navigation.forward(50)  #move towards objective A0
sleep(1.4)
Navigation.stop() #simulate button hit time
sleep(4)          #simulate completion of first objective
Navigation.backward(50) #return to center
sleep(1.4)
Navigation.stop()
sleep(1)
Navigation.turnright(47)    #turn towards plank
sleep(0.5)
Navigation.stop()
sleep(1)
Navigation.forward(50) #go forward to second objective
sleep(4)               #make it all the way to B
Navigation.stop()
sleep(1)
Navigation.turnright(47) #turn towards objective B1
sleep(0.5)
Navigation.stop()
sleep(1)
Navigation.forward(50) #go towards B1
sleep(1.4)
Navigation.stop()     #stop after hitting B1
sleep(1)
Navigation.backward(50) #move back towards the middle of the route
sleep(1.4)
Navigation.stop()
sleep(1)
Navigation.turnleft(47) #face forward
sleep(0.5)
Navigation.stop()
sleep(1)
Navigation.backward(50) #cross the plank back up to complete C
sleep(5.4)               
Navigation.stop()
sleep(1)
Navigation.turnleft(47) #turn toward objective C0
sleep(0.5)
Navigation.stop()
sleep(1)
Navigation.forward(50)  #move to objective C0
sleep(1.4)
Navigation.stop()
cleanup()
