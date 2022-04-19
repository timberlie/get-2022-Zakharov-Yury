import RPi.GPIO as GPIO
from time import time, sleep
from math import sin


a = 100 * (float(input()) / 3.28)
frequency = 50

out_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(out_pin, GPIO.OUT)


try:
    start = time()
    while True:
        # a = 50 * (1 + sin(time()))
        if ((start - time()) % (1 / frequency)) < (1 / frequency) * (a / 100):
            GPIO.output(out_pin, 1)
        else:
            GPIO.output(out_pin, 0)
finally:
    GPIO.output(out_pin, 0)
    GPIO.cleanup()