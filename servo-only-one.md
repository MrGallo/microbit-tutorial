# Servo Motor (only one)

I say "only one" because at the time of writing this, I believe the 3V power supply of the microbit is barely enough to power one servo and may not be cable to power multiple. We have the ability to attach an external power source to the breakout boards when necessary.

```python
# Imports go at the top
from microbit import *

def set_servo_angle(pin, angle):
    duty = 26 + (angle * 102) / 180
    pin.write_analog(duty)


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        set_servo_angle(pin0, 0)
        display.show(Image.ARROW_W)
    elif button_b.was_pressed():
        set_servo_angle(pin0, 180)
        display.show(Image.ARROW_E)
```

## Button A points it Left
![image](https://user-images.githubusercontent.com/11080017/221912677-26516d6e-96e4-4b9c-8b3b-5a7ce08da207.png)

## Button B points it Right
![image](https://user-images.githubusercontent.com/11080017/221912810-4728fff2-0e95-48e1-9586-53fc0b3d395d.png)
