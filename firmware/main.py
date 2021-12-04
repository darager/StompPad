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
            keeb = self.keyboard
            keys = self.keys

            keeb.press(*keys)
            keeb.release(*keys)

        self.lastPinState = currState


k = keyboard.Keyboard()

alt = k.MOD_LEFT_ALT
alt_i = [alt, 0x0c]
alt_j = [alt, 0x0d]
alt_k = [alt, 0x0e]
alt_l = [alt, 0x0f]
alt_u = [alt, 0x18]

switches = [
            Switch(17, alt_i, k), Switch(16, alt_u, k),
    Switch(20, alt_j, k), Switch(19, alt_k, k), Switch(18, alt_l, k)
]

while True:
    for switch in switches:
        switch.checkForInputValueChange()

    time.sleep(0.05)