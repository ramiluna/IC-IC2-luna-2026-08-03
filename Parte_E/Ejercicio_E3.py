import csv
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funciones import calcular_promedio as promedio

ruta_csv = os.path.join(os.path.dirname(__file__), 'peliculas.csv')

puntajes = []
mejor_titulo = None
mejor_puntaje = None

with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        puntaje_actual = float(fila['puntaje'])
        puntajes.append(puntaje_actual)

        if mejor_puntaje is None or puntaje_actual > mejor_puntaje:
            mejor_puntaje = puntaje_actual
            mejor_titulo = fila['titulo']

cantidad_peliculas = len(puntajes)
promedio_puntajes = promedio(puntajes)

print(f"Cantidad de películas: {cantidad_peliculas}")
print(f"Puntaje promedio: {promedio_puntajes:.1f}")
print(f"Mejor puntuada: {mejor_titulo} ({mejor_puntaje})")