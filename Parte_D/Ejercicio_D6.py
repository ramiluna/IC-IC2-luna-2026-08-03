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

def reporte(notas):
    datos = estadisticas(notas)
    return f"Promedio: {datos['promedio']:.1f} | Máximo: {datos['maximo']} | Mínimo: {datos['minimo']}"

# Pruebo la función
lista1 = [7, 4, 9, 10]

print(reporte(lista1))