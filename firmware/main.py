import time
import keyboard
from machine import Pin

led = Pin(25, Pin.OUT)
button = Pin(16,  Pin.IN, Pin.PULL_UP)

k = keyboard.Keyboard()
a = 0x04;

prev = False

while True:
    time.sleep(0.05)

    curr = not button.value()

    led.value(curr)

    if prev == False and curr == True:
        k.press(a)
        k.release_all()

    prev = curr