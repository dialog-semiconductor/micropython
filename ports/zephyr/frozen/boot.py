import time
from machine import Pin

print("Frozen Boot!")

led = Pin(("gpio@50020a00", 26), Pin.OUT)

i = 0
while i < 10:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    i += 1
