pares = 0
impares = 0

for alumno in range(1, 31):
    if alumno % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Alumnos con número par: {pares}")
print(f"Alumnos con número impar: {impares}")
print(f"Total revisado: {pares + impares}")