# Imports go at the top
from microbit import *

x = 2
y = 4

# Code in a 'while True:' loop repeats forever
while True:   
    if button_b.was_pressed():
        x += 1

    # prevent movement passed right wall
    if x == 5:
        x = 4
    
    # do button a code
    if button_a.was_pressed():
        x -= 1

    if x == -1:
        x = 0
    
    # draw player
    display.clear()
    display.set_pixel(x, y, 9)

    sleep(33)
