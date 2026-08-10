import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from funciones import calcular_promedio as promedio

# Pruebo con una lista vacía
resultado = promedio([])
print(f"Resultado con lista vacía: {resultado}")

# Pruebo también que sigue funcionando normal con una lista con datos
resultado2 = promedio([7, 4, 9, 10])
print(f"Resultado con lista normal: {resultado2}")