import csv
import os

ruta_csv = os.path.join(os.path.dirname(__file__), 'peliculas.csv')

suma_puntajes = 0

with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        puntaje = float(fila['puntaje'])
        suma_puntajes += puntaje

print(f"Suma total de puntajes: {suma_puntajes:.1f}")