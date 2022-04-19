import matplotlib.pyplot as plt

voltage = [0.0, 1.3, 2.09, 2.56, 2.85, 3.03, 3.14, 3.2, 3.24, 3.26]

with open('data.txt', 'w') as outfile:
    plt.plot(voltage)
    plt.xlabel('t, с')
    plt.ylabel('U, В')
    plt.title('Зависимость напряжения на обкладках конденсатора U от времени t')
    plt.show()
    
    str_voltage = [str(u) for u in voltage]
    out = '\n'.join(str_voltage)
    outfile.write(out)