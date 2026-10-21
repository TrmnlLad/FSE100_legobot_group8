# FSE100 Legobot - Group 8

Our LEGO EV3 robot for FSE100. You drive it from a laptop keyboard over wifi.

main.py runs on the EV3 brick (pybricks micropython). It waits for a connection on port 12345 and drives the motors on ports C and D. The touch sensor kill switch goes on port 1. If it isn't plugged in the robot still drives.

Client_control.py runs on the laptop and sends the key presses. Before running it, change EV3_IP to whatever IP the brick shows.

kill_switch.py is just a quick test for the touch sensor. It beeps until you press it.

Controls: W and S drive forward and back, A and D turn, Q quits.

To run it:

```
pip install -r requirements.txt
```

Start main.py on the EV3 first, then run `python Client_control.py` on the laptop.

Pressing the kill switch stops the robot and the brick beeps. You have to restart main.py after that.
