peliculas = [
    {
        "titulo": "Interestelar",
        "anio": 2014,
        "director": "Christopher Nolan"
    },
    {
        "titulo": "Jurassic Park",
        "anio": 1993,
        "director": "Steven Spielberg"
    },
    {
        "titulo": "Toy Story",
        "anio": 1995,
        "director": "John Lasseter"
    }
]

director_buscado = "Christopher Nolan"
encontrada = False

for pelicula in peliculas:
    if pelicula["director"] == director_buscado:
        print(pelicula["titulo"])
        encontrada = True

if not encontrada:
    print("No se encontraron películas de ese director.")
