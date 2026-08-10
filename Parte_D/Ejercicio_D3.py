import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones import calcular_promedio as promedio

def estadisticas(notas):
    return {
        "promedio": promedio(notas),
        "maximo": max(notas),
        "minimo": min(notas)
    }

# Pruebo la función con una lista
lista1 = [7, 4, 9, 10]

resultado = estadisticas(lista1)
print(f"Estadísticas de {lista1}:")
print(resultado)