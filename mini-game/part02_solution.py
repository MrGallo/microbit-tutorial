# Imports go at the top
from microbit import *
import random

"""
1. Create x and y variables for your falling object. 
   Set them to a random location along the top.
   Use display.set_pixel to see it on the screen.
2. We need to move the object down every second. To do this
   we keep track of the number of frames with a frame_count variable.
   Increase the frame_count by 1 every loop.
   Print it out.
3. If the frames == 30, then move the object down. Reset the frame count to 0.
4. If the object reaches the bottom, move it back to the top
   at a random location.
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

