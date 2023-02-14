# Imports go at the top
from microbit import *
import random

"""
1. Create a score variable. Set it to 0. Every time the object hits the bottom, add one to the score.
   Print the score out when that happens (not every loop).
2. When the object hits the player, print out "HIT".
3. When the player is hit, 'break' out of the loop to end the game.
4. Display the score when you lose.
"""

# player position
x = 2
y = 4

# object position
obj_x = random.randrange(0, 5)
obj_y = 0

frame_count = 0

# Code in a 'while True:' loop repeats forever
while True:
    frame_count += 1

    if frame_count == 30:
        obj_y += 1
        frame_count = 0

    if obj_y == 5:
        obj_y = 0
        obj_x = random.randrange(0, 5)
    
    if button_b.was_pressed():
        x += 1

    if x == 5:
        x = 4

    if button_a.was_pressed():
        x -= 1

    if x == -1:
        x = 0
    
    display.clear()
    
    # draw player
    display.set_pixel(x, y, 9)

    # draw object
    display.set_pixel(obj_x, obj_y, 9)

    sleep(33)

