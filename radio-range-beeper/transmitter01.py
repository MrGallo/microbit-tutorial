from microbit import *
import radio

radio.config(group=0, power=6)

display.scroll("Tx")

while True:
    radio.send("hello")
    display.show(Image.YES)

    if button_a.was_pressed() and button_b.was_pressed():
        break
        
    sleep(1000)

radio.off()
display.scroll("Off")
