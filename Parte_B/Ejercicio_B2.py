# 1. Importo la lista de canciones de la playlist del Ejercicio B1. 
from Ejercicio_B1 import playlist 
# 2. Aca agrego dos canciones mas de mi preferencia, ambas se agregan a la ultima posicion.
playlist.append ("El revelde")
playlist.append("La balada del diablo y la muerte")
# 3. compurebo la lista de la playlist para ver si se han agregado las canciones. 
print(f"\nLa playlist ahora contiene {len(playlist)} canciones")
print(playlist)
# 4. Accedo a una posicion x.
print("\nCancion en la posicion 6:")
print(playlist[6])