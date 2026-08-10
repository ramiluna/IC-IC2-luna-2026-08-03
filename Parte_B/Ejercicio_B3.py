puntajes= [120, 45,300,80,210]
mayor= puntajes[0]
menor= puntajes[0]
#2. recorro la lista con un bucle for.
for puntaje in puntajes:
    #3. Chequeo si encuentro algun valor nuevo para mayor.
    if puntaje > mayor: 
        mayor=puntaje
    #4 Chequeo los menores. 
    if puntaje < menor:
        menor=puntaje
    #5. Acumulo la suma de todos los puntajes para el calculo del promedio. 
    Suma_Total = sum(puntajes)
#6. Calculo el prom. 
promedio = sum(puntajes) / len(puntajes)
#7. imprimo los resultados manuales. 
print("Resultados usando el bucle 'for':")
print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")
print(f"El promedio es: {promedio}")
#8. Comparo con las funciones max , min de python. 
print("\nValidación con max() y min():")
print(f"El mayor con max() es: {max(puntajes)}")
print(f"El menor con min() es: {min(puntajes)}")
