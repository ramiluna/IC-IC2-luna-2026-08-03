Titulo_1 = {
    "titulo":"TOY STORY",
    "año": 2023
}
Titulo_2 = { 
    "puntaje" : 10, 
    "año": 2026
}
pelicula_completa = Titulo_1 | Titulo_2

print(pelicula_completa)
# Siempre que se compare gana el valor del diccionario de la derecha si ambos comparten la misma key, por ejemplo ahora cambio el orden, usando update. 
Titulo_2.update(Titulo_1)
print(Titulo_2)