import csv
import os

ruta_csv = os.path.join(os.path.dirname(__file__), 'peliculas.csv')
ruta_filtradas = os.path.join(os.path.dirname(__file__), 'filtradas.csv')

genero_elegido = "Ciencia Ficcion"

peliculas_filtradas = []

with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        if fila['genero'] == genero_elegido:
            peliculas_filtradas.append(fila)

with open(ruta_filtradas, mode='w', encoding='utf-8', newline='') as archivo_nuevo:
    columnas = ['titulo', 'puntaje', 'genero']
    escritor = csv.DictWriter(archivo_nuevo, fieldnames=columnas)
    escritor.writeheader()
    escritor.writerows(peliculas_filtradas)

print(f"Se filtraron {len(peliculas_filtradas)} películas de género '{genero_elegido}'.")
print(f"Guardadas en: {ruta_filtradas}")