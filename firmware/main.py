import time
import keyboard
from keyboard import Key
from machine import Pin

k = keyboard.Keyboard()

class Switch:
    def __init__(self, pinId, onPress):
        self.pin = Pin(pinId, Pin.IN, Pin.PULL_UP)
        self.lastPinState = not self.pin.value()
        self.onPress = onPress

    def checkForInputValueChange(self):
        currState = not self.pin.value()

        if self.lastPinState == False and currState == True:
            if self.onPress:
                self.onPress()

        self.lastPinState = currState

def createSendFunc(keys, keeb):
    def send():
        keeb.press(*keys)
        keeb.release(*keys)
    return send

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

    keys = layers["default"][i]
    send = createSendFunc(keys, k)

    switch = Switch(pin, send)
    switches.append(switch)

while True:
    for switch in switches:
        switch.checkForInputValueChange()

    time.sleep(0.05)