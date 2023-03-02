# ADKeys in Python

When attached to a pin on the breakout board, the buttons are read using `read_analog()`. This will return
different values based on what button is being pressed. Different hardware may have different results, so check it.

I atteched the ADKeys to `pin0`, so either do that or change the `read_analog()` line.

```python
from microbit import *

# The values appearing on my microbit are as follows,
# your values may be different. Run the program and verify
# the output values when you press the buttons.
KEY_A = 3
KEY_B = 53

# See if you can figure out the remaining buttons yourself.


while True:
    value = pin0.read_analog()
    print(value)

    if value == KEY_A:
        display.show("A")
    elif value == KEY_B:
        display.show("B")
    else:
        display.show(Image.DIAMOND_SMALL)

    if button_a.was_pressed():
        break

    sleep(30)


print("DONE")
```
