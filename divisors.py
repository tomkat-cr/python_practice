# divisors.py
# 2022-07-01 | CR

def divisors(number_to_evaluate):
    if number_to_evaluate < 1:
        raise ArithmeticError('Sólo se aceptan números mayores que cero.')
    divisors = ''
    for numero in range(1, number_to_evaluate+1):
        try:
            if number_to_evaluate % numero == 0:
                divisors += (', ' if divisors != '' else '') + str(numero)
        except BaseException as ve:
            divisors = 'ERROR [1]: ' + str(ve)
    if not 'ERROR' in divisors:
        divisors = 'El número \'' + str(number_to_evaluate) + '\' es divisible entre: ' + divisors
    return divisors


if __name__ == '__main__':
    try:
        number_to_test = int(input('Introduca un número: '))
        print(divisors(number_to_test))
    except ValueError:
        print('Número inválido. Sólo se aceptan números mayores que cero. No se aceptan números negativos.')
    except BaseException as ve:
        print('ERROR [2]: ' + str(ve))
