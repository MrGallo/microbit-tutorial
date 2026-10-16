 
# Imports go at the top
from microbit import *


x = 2

while True:
    if button_b.was_pressed():
        x += 1

    # prevent x from going too far right
    if x == 5:
        x = 4

    # press a, move left
    if button_a.was_pressed():
        x += -1
        
    # prevent x from going too far left

    # try it:
    # can you make the player wrap around rather than hit a wall?


    display.clear()
    display.set_pixel(x, 4, 9)
    sleep(33)
