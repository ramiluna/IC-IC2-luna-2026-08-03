# 1. Defino la playlist como una lista. 
playlist=["El terco", "Cruz diablo!","No More Tears","Salando las heridas","Ji ji ji"]
# Establezco que la procion siguiente de codigo se corra solamente si se solicita en este archivo, no si se importa algun valor de este ejercicio hacia otro archivo.
if __name__ == "__main__":
# 2. Imprimo todas las canciones disponibles en la lista.
    print("\n Playlist entera")
    print (playlist)
# 3. Imprimo la primer cancion que aparece en la lista
    print("\nPrimer cancion de la playlist:")
    print(playlist[0])
# 4. Imprimo la ultima cancion de la lista.
    print("\nUltima cancion de la playlist:")
    print(playlist[-1])