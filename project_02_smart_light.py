# PROJECT 02: SMART LIGHT

from microbit import *

pir_pin = pin0
blue_led = pin1
 
while True:
    movement = pir_pin.read_digital()
    print(movement)

    if movement == 1:
        blue_led.write_digital(1)
    else:
        blue_led.write_digital(0)
        
