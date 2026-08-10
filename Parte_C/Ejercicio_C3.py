pelicula = {
    "titulo": "Oppenheimer",
    "año": 2023,
    "director": "Christopher Nolan"
}
pelicula.get("duracion","desconocido")
print(pelicula.get("duracion", "desconocido"))
# si el valor si existe, el get lo imprime, sino, da el valor "desconocido" que le pedi yo que devuelva si es que no encuentra el pedido
print(pelicula.get("titulo", "desconocido"))