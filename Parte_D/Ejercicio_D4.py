import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones import calcular_promedio as promedio

def aprobo(notas, minimo=6):
    return promedio(notas) >= minimo

# Pruebo la función de las dos formas
lista1 = [7, 4, 9, 10]

# Sin pasar minimo, usa el valor por default (6), ya que no se especifica cual es el minimo.
print(f"Sin especificar mínimo: {aprobo(lista1)}")

# Pasando minimo=7, aca lo que hace es usar ese valor, en vez del default
print(f"Con mínimo=7: {aprobo(lista1, minimo=7)}")