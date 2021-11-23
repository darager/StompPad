import time
from machine import Pin
import pyb

kb = pyb.USB_HID()
# pyb.delay(5)
# # Do the key up
# buf[0] = 0x00
# buf[2] = 0x00
# kb.send(buf)

pin = Pin(5, Pin.IN, Pin.PULL_UP)

while True:
    time.sleep(1)
    value = pin.value() # if value is 0 button is pressed
    print(time.ticks_ms(), value)

    if value == 0:
        buf = bytearray(8)
        # Sending T
        # Do the key down
        buf[0] = 0x02 # LEFT_SHIFT
        buf[2] = 0x17 # keycode for 't/T'
        kb.send(buf)
