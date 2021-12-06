import time
import keyboard
from keyboard import Key
from machine import Pin


class DebouncedSwitch:
    def __init__(self, pin, pinOnState = 0, debounceTime = 5):
        self.pin = pin
        self.pinOnState = pinOnState
        self.debounceTime = debounceTime
        self.lastState = self.pin.value()
        self.OnPressed = []
        self.OnReleased = []
        pin.irq(self.handleInterrupt, Pin.IRQ_RISING | Pin.IRQ_FALLING)

    def _wait_pin_change(self):
        # wait for pin to change value
        # it needs to be stable for the debounceTime
        sTime = self.debounceTime / 1000
        cur_value = self.pin.value()
        active = 0
        while active < 20:
            if self.pin.value() != cur_value:
                active += 1
            else:
                active = 0
            time.sleep(sTime)

    def handleInterrupt(self, pinInfo):
        self._wait_pin_change()
        currentState = self.pin.value()

        if self.lastState is not self.pinOnState and currentState is self.pinOnState:
            for f in self.OnPressed:
                f()
        else:
            for f in self.OnReleased:
                f()

        self.lastState = currentState


alt = Key.MOD_LEFT_ALT
alt_i = [alt, Key.i]
alt_j = [alt, Key.j]
alt_k = [alt, Key.k]
alt_l = [alt, Key.l]
alt_u = [alt, Key.u]

keeb = keyboard.Keyboard()
currentLayer = "default"

def layer(layerName):
    def swapLayer():
        currentLayer = layerName
    return swapLayer

switchPins = [ 17, 16, 20, 19, 18]

keybindings = {
    "default":      [ alt_i, alt_u, alt_j, alt_k, layer("default_hold") ],
    "default_hold": [ Key.I, Key.U, Key.J, Key.K, layer("default") ]
}

def handleBinding(keybinding):
    if keybinding is None:
        return

    print(keybinding)
    # currently have no way of telling if typeof Function
    # try:
    #     keybinding()
    # except:
    #     keys = keybinding
    #     keeb.press(*keys)
    #     keeb.release(*keys)

def getBinding(idx, layerName):
    return keybindings[layerName][idx]


def onpress():
    binding = getBinding(0, "default")
    handleBinding(binding)

pin = Pin(17, Pin.IN, Pin.PULL_UP)
debSwitch = DebouncedSwitch(pin);
debSwitch.OnPressed.append(onpress)