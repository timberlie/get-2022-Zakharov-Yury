import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

leds =    [26, 19, 13, 6, 5, 11, 9, 10]
pattern = [0,  0,  0,  0, 0,  0, 0,  0]

GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, pattern)


def decimal2binary(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]

try:
    count = 0
    flag = 'up'
    while True:
        GPIO.output(leds, decimal2binary(count))
        T = 5
        sleep(T / 480)
        
        if flag == 'up':
            if count < 240:
                count += 1
            else:
                flag = 'down'
        else:
            if count > 0:
                count -= 1
            else:
                flag = 'up'
finally:
    GPIO.output(leds, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()