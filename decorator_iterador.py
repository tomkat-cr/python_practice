# decorator_iterador.py
# 2021-11-01 | D Andrés Rojas
# Plantee otra solución para iterar n elementos.
# Con la ayuda de una función recursiva y un decorador.


def iterador(func):
	def wrapper(lista):
		lista = iter(lista)
		func(lista)
	return wrapper


@iterador
def iterame(lista):
	try:
		print(next(lista))
		return iterame(lista)
	except StopIteration:
		pass


iterame('Platzi<3')
