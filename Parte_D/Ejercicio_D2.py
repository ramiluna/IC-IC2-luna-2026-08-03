import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones import calcular_promedio as promedio

def aprobo(notas):
    return promedio(notas) >= 6

# Pruebo la función con dos listas distintas
lista1 = [7, 4, 9, 10]
lista2 = [3, 4, 5, 4]

print(f"lista1: {lista1} -> ¿Aprobó? {aprobo(lista1)}")
print(f"lista2: {lista2} -> ¿Aprobó? {aprobo(lista2)}")