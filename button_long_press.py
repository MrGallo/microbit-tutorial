# Imports go at the top
from microbit import *


LONG_FRAMES = 15  # 0.5 second
press_frames = 0

while True:
    if button_b.is_pressed():
        press_frames += 1
        display.show("B")
    else:
        if press_frames > LONG_FRAMES:
            display.scroll("LB")
            print("Long-press B")
        elif press_frames > 0:
            display.scroll("SB")
            print("press SB")
            
        press_frames = 0
        display.show("X")
    
    print(press_frames)
    sleep(33)