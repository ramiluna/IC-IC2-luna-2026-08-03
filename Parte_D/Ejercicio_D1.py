import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones import calcular_promedio as promedio

# Pruebo la función con dos listas distintas
lista1 = [7, 4, 9, 10]
lista2 = [15, 20, 18, 22, 19]

print(f"Promedio lista1: {promedio(lista1):.1f}")
print(f"Promedio lista2: {promedio(lista2):.1f}")