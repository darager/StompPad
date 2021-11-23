import time
from machine import Pin

pin = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    time.sleep(1)
    value = pin.value() # if value is 0 button is pressed
    print(time.ticks_ms(), value)