import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
try:
    while True:
        value = input('Введите число от 0 до 100 ')
        p = GPIO.PWM(22,50)
        p.start(int(value))
        print(3.3 / 100 * int(value))
        p.stop()

finally:
    GPIO.cleanup()