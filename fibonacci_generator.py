# fibonacci_generator.py
# 2022-07-02 | CR
# Serie de Fifonacci resuleta con Generators

import time 

def fibo_gen(stop=None):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if stop and aux > stop:
                break
            n1, n2 = n2, aux
            counter += 1
            yield aux
        # Cuando no devuelve mas nada con yield, se termina la iteraccion...


if __name__ == '__main__':
    # fibonacci = fibo_gen()
    fibonacci = fibo_gen(21)
    for element in fibonacci:
        print(element)
        time.sleep(1)
