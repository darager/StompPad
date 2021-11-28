import time
import keyboard
from machine import Pin

led = Pin(25, Pin.OUT)
button = Pin(16,  Pin.IN, Pin.PULL_UP)

k = keyboard.Keyboard()
a = 0x04;

while True:
    time.sleep(0.1)
    led.value(button.value())

    if not button.value():
        k.press(a)
        k.release();