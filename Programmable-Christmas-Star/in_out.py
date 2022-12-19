from star import Star
from time import sleep

star = Star()

try:
    star.inner.on()
    while True:
        star.toggle()
        sleep(0.5)
except KeyboardInterrupt:
    star.close()
