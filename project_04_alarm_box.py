# IMPORTANT
# You will need the ssd1306.py file to run along side this one.

from microbit import *
from ssd1306 import SSD1306


# Initialize the OLED display
WIDTH = 128
HEIGHT = 64
i2c_addr = 0x3C  # Default I2C address for the OLED
oled = SSD1306(WIDTH, HEIGHT, i2c, addr=i2c_addr)

# Function to display text on the OLED screen

oled.fill(0)  # Clear the screen
oled.text("Hello world!", 0, 0)  # Display the text at the top-left corner
oled.show()
