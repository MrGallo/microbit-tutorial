"""
Intro to using Servos with the Monk Makes Servo Kit
Follow the instructions in the manual.
This is a test program inspired by the manual.
"""

from microbit import *


def angle_to_duty(angle: float) -> int:
    """Converts an angle in degrees to a duty cycle.

    Args:
        angle (float): The angle to convert

    Returns:
        (int) Duty cycle.
    """
    return int(26 + (angle * 102) / 180)


display.scroll("svo")

pin0.write_analog(angle_to_duty(180/3))
sleep(1000)
pin1.write_analog(angle_to_duty(180*2/3))
sleep(1000)
pin2.write_analog(angle_to_duty(180))
sleep(1000)

