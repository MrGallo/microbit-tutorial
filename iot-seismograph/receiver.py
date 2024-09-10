from microbit import *
import radio


radio.config(group=19)
radio.on()
while True:
    message = radio.receive()
    if message:
        display.scroll(message)
