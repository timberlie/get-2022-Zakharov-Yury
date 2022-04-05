import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

max_vol = 3.3
levels = 256
troyka = 17
comp = 4

GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]


def adc():
    for value in range(256):
            signal = decimal2binary(value)
            GPIO.output(dac, signal)
            voltage = value / levels * max_vol
            time.sleep(0.005)
            comp_value = GPIO.input(comp)
            
            if comp_value == 0:
                
                return voltage
                break

try:
    GPIO.output(troyka, 1)
    while True:
        vol = adc()
        print("input voltage = {:.2f}".format(vol))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)