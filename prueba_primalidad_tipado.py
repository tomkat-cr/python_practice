# prueba_primalidad_tipado.py
# 2022-06-25 | CR
from math import factorial

def evalua_numero_primo_eficiente(numero_evaluado : int) -> bool:
    print('Con el Teorema de Wilson...')
    if numero_evaluado <= 1:
        return False
    n = factorial(numero_evaluado-1)+1
    return (n % numero_evaluado == 0)


def run():
    while True:
        numero_a_evaluar_input : str = input("Introduce un número para ver si es primo: ")
        try:
            numero_a_evaluar : int = int(numero_a_evaluar_input)
        except ValueError:
            print('ERROR: Debe introducir un valor numérico')
        else:
            break
    if True:
    # if False:
        es_primo : bool = evalua_numero_primo_eficiente(numero_a_evaluar)
    else:
        es_primo = evalua_numero_primo_eficiente(numero_a_evaluar_input)
    msg_resultado : str = 'NO es primo'
    if es_primo:
        msg_resultado = 'es primo'
    print('El número ' + str(numero_a_evaluar) + ' ' + msg_resultado)


if __name__ == '__main__':
    run()