import time
import keyboard
from machine import Pin

class Switch:
    def __init__(self, pinId, keys, keyboard):
        self.keyboard = keyboard
        self.keys = keys

        self.pin = Pin(pinId, Pin.IN, Pin.PULL_UP)
        self.lastPinState = not self.pin.value()

    def checkForInputValueChange(self):
        currState = not self.pin.value()

        if self.lastPinState == False and currState == True:
            for key in self.keys:
                self.keyboard.press(key)
            for key in self.keys:
                self.keyboard.release(key)

        self.lastPinState = currState

k = keyboard.Keyboard()
switches = [
    Switch(16, [0x05], k)
]

while True:
    for switch in switches:
        switch.checkForInputValueChange()

    time.sleep(0.05)