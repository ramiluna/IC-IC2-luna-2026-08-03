import csv
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from funciones import calcular_promedio as promedio

ruta_csv = os.path.join(os.path.dirname(__file__), 'peliculas.csv')

# 1. Agrupo los puntajes por género
puntajes_por_genero = {}

with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        genero = fila['genero']
        puntaje = float(fila['puntaje'])

        if genero not in puntajes_por_genero:
            puntajes_por_genero[genero] = []

        puntajes_por_genero[genero].append(puntaje)

# 2. Calculo el promedio de cada género
promedio_por_genero = {}

for genero, lista_puntajes in puntajes_por_genero.items():
    promedio_por_genero[genero] = promedio(lista_puntajes)

# 3. Muestro el resultado
print(promedio_por_genero)