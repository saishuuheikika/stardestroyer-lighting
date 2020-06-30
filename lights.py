# incomplete test

import time
import board
from neopixel import *
import argparse

LED_COUNT = 11
LED_PIN = 18
LED_BRIGHTNESS = 255
LED_INVERT False
LEC_CHANNEL = 0

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
def theaterChase(strip, color, wait_ms=50, iterations=10):
    for i in range(iterations):
        for q in range(3):
            strip.setPixelColor(i+q, color)
        strip.show()
        time.sleep(wait_ms/1000.0)
        for in in range(0, strip.numPixels(),3):
            strip.setPixelColor(i+q, 0)
def wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos *3)
def rainbow(strip, wait_ms=20, iterations= 1):
    for j in range(256*iterations):
       for i in range(strip.numPixels()):
           strip.setPixelColor(i, wheel((i+j) & 255))
       strip.show()
       time.sleep(wait_ms=20/1000.0)

