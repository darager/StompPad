import time
import keyboard
from keyboard import Key
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

alt = Key.MOD_LEFT_ALT
alt_i = [alt, Key.i]
alt_j = [alt, Key.j]
alt_k = [alt, Key.k]
alt_l = [alt, Key.l]
alt_u = [alt, Key.u]

switchPins = [ 17, 16,
             20, 19, 18]
layers = {
    "default": [ alt_i, alt_u,
              alt_j, alt_k, alt_l ]
}

switches = []

for i in range(len(switchPins)):
    pin = switchPins[i]
    switch = Switch(pin, layers["default"][i], k)
    switches.append(switch)

while True:
    for switch in switches:
        switch.checkForInputValueChange()

    time.sleep(0.05)