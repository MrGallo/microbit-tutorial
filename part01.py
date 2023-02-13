# Imports go at the top
from microbit import *

x = 2
y = 4

# Code in a 'while True:' loop repeats forever
while True:
    # 1. Prevent player from moving
    #    beyond the right wall.
    # 2. Add button_a functionality.
    
    if button_b.was_pressed():
        x += 1

    if x == 5:
        x = 0
    
    # draw player
    display.clear()
    display.set_pixel(x, y, 9)

    sleep(33)
