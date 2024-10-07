# Project 01: MUSIC MACHINE

from microbit import *
import music

buzzer_pin = pin0
buttons_pin = pin2
 
# Code in a 'while True:' loop repeats forever
while True:

    if button_a.was_pressed():
        music.pitch(784, duration=1000)

    value = buttons_pin.read_analog()
    print(value)
    if value == 3:  # play C
        music.pitch(523, duration=1000)
        
    # C = 523
    # D = 587
    # E = 659
    # F = 698
    # G = 784
