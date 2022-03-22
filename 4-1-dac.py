import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
duc = [26, 19, 13, 6, 5, 11, 9, 10]
value = [0,0,0,0,0,0,0,0]

GPIO.setup(duc, GPIO.OUT)
GPIO.output(duc, value)

def decimal2binary(value):
    return [int(element) for element in bin(int(value))[2:].zfill(8)]

try:
    while True:
        value = input('Введите число от 0 до 255: ')
        if value == "q":
            break
        else:
            flag = 1
            for item in value:
                if item.isdigit() != True:
                    if item == ".":
                        print('Введено не целое значение')
                    elif item == "-":
                        print("Введено отрицательное значение")
                    else:
                        print('Введено не числовое значение')
                    flag = 0
                    break
            if flag and len(decimal2binary(value)) > 8:
                print('Превышение разряда')
                flag = 0
        if flag:
            GPIO.output(duc, decimal2binary(value))
            print(3.3 / 256 * int(value))
finally:
    GPIO.output(duc, [0, 0, 0, 0, 0, 0, 0, 0])
    GPIO.cleanup()
