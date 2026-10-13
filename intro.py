from microbit import *

display.scroll("hello")

while True:
    if button_a.is_pressed():
        display.show("A")
    elif pin0.is_touched():
        display.show("0")
    else:
        display.show("X")

    sleep(33)

"""
Flashing code to microbit
-------------------------
1. Connect the microbit to the computer with the USB cable.
2. Click "..." on the code editor. Choose "connect".
3. Follow on-screen instructions.
4. Click "Send to microbit.
"""
