
import sys
import os

# Agrega la raíz del proyecto al path, sin importar desde dónde ejecutes el archivo
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import funciones
print (funciones.__file__)

from funciones import calcular_promedio

notas = [7, 4, 9, 10]
promedio = calcular_promedio(notas)
print(f"{promedio:.1f}")