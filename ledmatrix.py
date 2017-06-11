import time
import RPi.GPIO as GPIO

#import the WS# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Configure the count of pixels:
PIXEL_COUNT = 42
 
# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

color1 = [255, 0, 0]
color2 = [0, 0, 255]

def draw (vector):
    for i in range (0, 41):
        if (vector[i] == 1):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(color1[0], color1[1], color1[2]))
        elif (vector[i] == 2):
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(color2[0], color2[1], color2[2]))
        else:
            pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(0, 0, 0))
    pixels.show()
