from servo_control import *

def staighten():
    wrist.SetAngle(90)

def approachWheel():
    rotate.SetAngle(0)
    claw.SetAngle(180)

def turnWheel():
    claw.SetAngle(0)
    rotate.SetAngle(270)
    claw.SetAngle(180)


