# ADKeys in Python

When attached to a pin on the breakout board, the buttons are read using `analog_read()`. This will return
different values based on what button is being pressed. Different hardware may have different results, so check it.

```python
from microbit import *

# The values appearing on my microbit are as follows,
# your values may be different. Run the program and verify
# the output values when you press the buttons.
KEY_A = 3
KEY_B = 53
KEY_C = 98
KEY_D = 139
KEY_E = 544

while True:
    read = pin0.read_analog()
    print(read)

    if read == KEY_A:
        display.show("A")
    elif read == KEY_B:
        display.show("B")
    elif read == KEY_C:
        display.show("C")
    elif read == KEY_D:
        display.show("D")
    elif read == KEY_E:
        display.show("E")
    else:
        display.show(Image.DIAMOND_SMALL)

    if button_a.was_pressed():
        break

    sleep(30)


print("DONE")
```
