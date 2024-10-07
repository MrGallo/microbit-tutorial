# Project 01: MUSIC MACHINE

from microbit import *

pir_pin = pin0
blue_led = pin1
 
# Code in a 'while True:' loop repeats forever
while True:
    movement = pir_pin.read_digital()
    print(movement)

    if movement == 1:
        blue_led.write_digital(1)
    else:
        blue_led.write_digital(0)
        
