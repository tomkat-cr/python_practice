# iterador_EvenNumbers.py

class EvenNumbers:
  """Clase que implementa un iterador de todos los números pares,
     o los números pares hasta un máximo
  """
  # Constructor de la clase
  #
  def __init__(self, max = None): # self hace referencia al objeto futuro que voy a crear con esta clase
    self.max = max


  # Método para tener elementos o atributos que voy a necesitar para que el iterador funcione
  #
  def __iter__(self):
    self.num = 0 # Primer número par
    # Convertir un iterable en un iterador
    return self


  # Método para tener la función "next" de Python
  #
  def __next__(self):
    if not self.max or self.num <= self.max:
      result = self.num
      self.num += 2
      return result
    else:
      raise StopIteration


if __name__ == "__main__":
    even_numbers = EvenNumbers(100)
    for element in even_numbers:
        print(element)
