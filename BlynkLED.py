# Packages
import BlynkLib
from rpi_ws281x import *

# LED Setup
LED_COUNT = 15
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 25
LED_INVERT = False
LED_CHANNEL = 0

RED = 0
GREEN = 0
BLUE = 0

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

BLYNK_AUTH = 'authcode'

# Initialise Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Put all definitions here
def SetSolid(red, green, blue):
	for x in range(0, LED_COUNT):
		strip.setPixelColor(x, Color(red, green, blue))
	strip.show()

# Register virtual pin, these respond kind of like events whenever there is a state change
@blynk.VIRTUAL_WRITE(0)
def v2_write_handler(value):
	print('Current value: {}').format(value[0])

while True:
	blynk.run()