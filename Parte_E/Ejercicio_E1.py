import csv
import os

# Ruta al archivo CSV, en la misma carpeta que este script
ruta_csv = os.path.join(os.path.dirname(__file__), 'peliculas.csv')

with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)