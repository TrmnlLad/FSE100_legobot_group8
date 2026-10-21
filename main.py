#!/usr/bin/env pybricks-micropython
# main.py
import socket
import _thread
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait


# Initialize EV3 components
ev3 = EV3Brick()
left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
# weapon = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Kill switch: touch sensor on input port 1.
# A background thread waits for it to be pressed, then stops the robot and beeps.
killed = False
running = True


def watch_kill_switch():
    global killed
    while not kill_switch.pressed():
        if not running:
            return  # main program ended
        wait(20)
    killed = True
    robot.stop()
    ev3.speaker.beep(1000, 500)
    print("Kill switch engaged")
    ev3.screen.print("Kill switch engaged")


try:
    kill_switch = TouchSensor(Port.S1)
    _thread.start_new_thread(watch_kill_switch, ())
except OSError:
    print("No kill switch on port 1")  # driving still works


# Server configuration
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Allow restarting right away without "address in use"
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", 12345))
server_socket.listen(1)
print("Waiting for connection...")
client_socket, address = server_socket.accept()
print("Connected to {}".format(address))


try:
    while True:
       
        command = client_socket.recv(2).decode()
        if not command or killed:
            break


        key, action = command[0], command[1]
        if action == "d":  # Key press
            if key == "w":
                robot.drive(900, 0)  # Move forward
            elif key == "s":
                robot.drive(-900, 0)  # Move backward
            elif key == "a":
                robot.drive(0, -450)  # Turn left
            elif key == "d":
                robot.drive(0, 450)  # Turn right
            #elif key == "f":
            #    weapon.run(1000)  # Spin weapon motor at max speed
        elif action == "u":  # Key release
            if key in ("w", "a", "s", "d"):
                robot.stop()  # Stop the robot on key release
            #elif key == "f":
            #    weapon.stop()  # Stop the weapon motor on key release

        if killed:
            break  # Kill switch pressed while handling this command


finally:
    running = False
    robot.stop()
    client_socket.close()
    server_socket.close()


