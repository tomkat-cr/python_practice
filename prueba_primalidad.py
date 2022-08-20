# prueba_primalidad.py
# 2022-06-25 | CR
from math import factorial

def evalua_numero_primo_ineficiente(numero_evaluado):
    print('Con el metodo menos eficiente...')
    contador = 0
    if numero_evaluado == 1:
        return False
    # for numero in range(1, numero_evaluado+1):
    for numero in range(2, numero_evaluado):
        # if numero == 1 or numero == numero_evaluado:
        #     continue
        if numero_evaluado % numero == 0:
            print('Es divisible entre ' + str(numero))
            contador += 1
            break
    return (contador == 0)


def evalua_numero_primo_eficiente(numero_evaluado):
    print('Con el Teorema de Wilson...')
    if numero_evaluado <= 1:
        return False
    #
    # https://www.masscience.com/2019/10/27/es-posible-encontrar-una-formula-que-permita-comprobar-si-un-numero-es-primo/
    # Uno de los avances más significativos en una forma eficiente de saber si un numero es primo
    # es el llamado teorema de Wilson, en honor al Matemático Inglés: John Wilson (1741 – 1793).
    # El teorema de manera simple dice :
    # Un número n es primo si y solo si (n-1)! + 1 es múltiplo de n
    #
    # https://www.geeksforgeeks.org/factorial-in-python/

    n = factorial(numero_evaluado-1)+1
    return (n % numero_evaluado == 0)


def run():
    while True:
        numero_a_evaluar = input("Introduce un número para ver si es primo: ")
        # https://www.tutorialsteacher.com/python/string-isnumeric
        if numero_a_evaluar.isnumeric():
            break
        else:
            print('ERROR: Debe introducir un valor numérico')
    numero_a_evaluar = int(numero_a_evaluar)
    # es_primo = evalua_numero_primo_ineficiente(numero_a_evaluar)
    es_primo = evalua_numero_primo_eficiente(numero_a_evaluar)
    if es_primo:
        msg_resultado = 'es primo'
    else:
        msg_resultado = 'NO es primo'
    print('El número ' + str(numero_a_evaluar) + ' ' + msg_resultado)


if __name__ == '__main__':
    run()