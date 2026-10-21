#!/usr/bin/env pybricks-micropython
# Kill switch - Team: 

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor
from pybricks.parameters import Port

ev3 = EV3Brick()
kill_switch = TouchSensor(Port.S1)

while not kill_switch.pressed():
    ev3.speaker.beep(500, 100)

ev3.screen.print("Kill switch engaged")
