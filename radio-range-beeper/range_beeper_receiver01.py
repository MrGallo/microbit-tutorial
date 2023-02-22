# Imports go at the top
from microbit import *
import music

frames = 0
sound_on = True

beep_pause_time = 30  # in frames

while True:
    frames += 1
    
    a_pressed = button_a.is_pressed()
    b_pressed = button_b.is_pressed()
    both_pressed = a_pressed and b_pressed
    
    if both_pressed:
        break

    if frames == beep_pause_time:
        sound_on = not sound_on
        beep_pause_time -= 1
        if beep_pause_time <= 0:
            beep_pause_time = 1
        frames = 0

        print(beep_pause_time)

    pitch = 440 + (30 - beep_pause_time) * 2
    if sound_on:
        music.pitch(pitch)
    else:
        music.stop()
    


    sleep(33)

music.stop()
display.scroll("Off")
