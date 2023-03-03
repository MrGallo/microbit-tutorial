"""
Messing around with LED light, PIR (motion) Sensor and the switch (crash sensor).

- Press the switch to turn on the blue LED light.
- Detected motion by the PIR sensor will turn on the green LED.

There are two ways to get data from the switch, namely
the is_touched method (preferred), or the read_analog() method
which will return an unintuitive integer value. 3 or so for off and 
around 900 for on.

Pins are defined below.
"""
from microbit import *


blue_led_pin = pin0
switch_pin = pin1
pir_sensor_pin = pin2
green_led_pin = pin3


while True:

    # SWITCH AND BLUE LED
    is_touched_value = switch_pin.is_touched()
    # print(is_touched_value)

    read_analog_value = switch_pin.read_analog()
    # print(read_analog_value)

    if switch_pin.is_touched():
        blue_led_pin.write_digital(1)
    else:
        blue_led_pin.write_digital(0)

    # SENSOR AND GREEN LED
    pir_value = pir_sensor_pin.read_analog()
    print(pir_value)

    if pir_sensor_pin.read_digital():
        green_led_pin.write_digital(1)
    else:
        green_led_pin.write_digital(0)

    sleep(30)

    
