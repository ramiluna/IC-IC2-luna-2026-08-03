def calcular_promedio(notas):
    if len(notas) == 0:
        print("Aviso: no se puede calcular el promedio de una lista vacía.")
        return None
    return sum(notas) / len(notas) 