
lecturas = [10, 12, 14, 11, 13, 15, 16, 14, 12, 10]

promedios_moviles = []

for i in range(len(lecturas) - 2):
    ventana = lecturas[i:i+3]
    promedio_ventana = sum(ventana) / len(ventana)
    promedios_moviles.append(promedio_ventana)

print(f"Lecturas originales: {lecturas}")
print(f"Promedios móviles: {promedios_moviles}")
print(f"Cantidad de lecturas: {len(lecturas)}")
print(f"Cantidad de promedios: {len(promedios_moviles)}")
lecturas = [10, 12, 14, 11, 13, 15, 16, 14, 12, 10]

promedios_moviles = []

for i in range(len(lecturas) - 2):
    ventana = lecturas[i:i+3]
    promedio_ventana = sum(ventana) / len(ventana)
    promedios_moviles.append(promedio_ventana)

print(f"Lecturas originales: {lecturas}")
print(f"Promedios móviles: {promedios_moviles}")
print(f"Cantidad de lecturas: {len(lecturas)}")
print(f"Cantidad de promedios: {len(promedios_moviles)}")
