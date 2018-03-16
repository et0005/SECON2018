#!/usr/bin/python

import routeEngine.py
import IR_control.py

#read IR
#given route find config
#load config
#plug into route engine
#execute route via route engine

if IR_control.IR1.destA == 1:
    if IR_control.IR1.destB == 1:
        if IR_control.IR1.destC == 1:
            print("Wait for start signal\n")

else:
    print("Begin Route!\n")
    routeEngine.begin()
