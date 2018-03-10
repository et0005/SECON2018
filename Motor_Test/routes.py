#!/usr/bin/python
#
#            _______________________________________
#           |                 WHEEL                 |                  E
#           |                                       |                  |
#           |                                       |               N--+--S
#           |                                       |                  |
#           |                                       |                  W
#           |                                       |
#           |                                       |
#           |                TREASURE               |
#           |                  ___                  |
#           |                 |   |                 |
#           |                 |___|                 |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |    ||                           ||    |
#           |    ||  B                     B  ||    |
#           |    ||                           ||    |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |                                       |
#           |             ________                  |
#           |             \       \                 |
#           |              \  RAMP \                |
#           |_______________\       \_______________|
#           |                _______                |
#           |               |       |               |
#        C  | A             | START |             A |  C
#           |               |_______|               |
#           |_______________________________________|
#
#
#           IR Input at START:      North (0)   South (1)
#
#              MSB   --------------   LSB       Bin.     Route        Route
#    bit        4      3       2       1        #        #
#
#               1      1       1       1        15       N/A          WAIT
#               0      0       0       0        0        1            A : Left, B: Left, C: Left
#               0      0       0       1        1        2            A : Left, B: Left, C: Right
#               0      0       1       0        2        3            A : Left, B: Right, C: Left
#               0      0       1       1        3        4            A : Left, B: Right, C: Right
#               0      1       0       0        4        5            A : Right, B: Left, C: Left
#               0      1       0       1        5        6            A : Right, B: Left, C: Right
#               0      1       1       0        6        7            A : Right, B: Right, C: Left
#               0      1       1       1        7        8            A : Right, B: Right, C: Right
#
#    func.    Start    A       B       C             (Bin. + 1)
#

import routeEngine.py
import servo.py

IR[4] = [0, 0, 0, 0]

if IR[3] == 1:
    print("Wait for start signal\n")

else:
    print("Begin Route!\n")
    routeEngine.forward_a()
    routeEngine.backtrack_a()
    routeEngine.walk_the_plank()
    routeEngine.forward_b()
    routeEngine.backtrack_b()
    routeEngine.forward_chest()
    servo.spin_wheel()
    routeEngine.align_to_start()
    routeEngine.backtrack_to_start()
    routeEngine.forward_c()
    routeEngine.complete()