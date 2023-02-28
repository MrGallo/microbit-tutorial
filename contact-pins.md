# Contact Pins

We can check when there is a completed circuit between Ground and one of the pins. The code will display a number depending on which pin is pressed.

```python
# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if pin0.is_touched():
        display.show("1")
    elif pin1.is_touched():
        display.show("2")
    elif pin2.is_touched():
        display.show("3")
```

![image](https://user-images.githubusercontent.com/11080017/221903545-075988ec-6559-40e9-b50c-a6b1fadbf51c.png)
![image](https://user-images.githubusercontent.com/11080017/221903556-c7f2d16b-fe9d-471e-a251-40a3d27966c1.png)
