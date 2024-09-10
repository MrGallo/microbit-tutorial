from microbit import *
import radio


radio.config(group=19)
radio.on()

while True:
    if accelerometer.was_gesture('shake'):
        display.show(Image.CONFUSED)
        radio.send("EARTHQUAKE!!")
    else:
        display.show(Image.HAPPY)

    sleep(1000)
