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
    bin_p = decimal2binary(0)
    for i in range(8):
        bin_p[i] = 1
        GPIO.output(dac, bin_p )
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            bin_p[i] = 0
    return bin_p[0]*128 + bin_p[1]*64 + bin_p[2]*32 + bin_p[3]*16 + bin_p[4]*8 + bin_p[5]*4 + bin_p[6]*2 + bin_p[7]
            


try:
    GPIO.output(troyka, 1)
    while True:
        vol = adc() / 256 * 3.3
        print("input voltage = {:.2f}".format(vol))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)