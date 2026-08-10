# 1. Defino las notas en una lista. 
notas=[7,4,9,10]
# 2. Realizo los calculos correspodientes para poder calcular el promedio. 
suma=sum(notas)
Cantidad_De_Notas=len(notas)
promedio=sum(notas)/len(notas)
# 3. Imprimo mensaje correspondiente a los calores de notas obtenidos 
if promedio >= 6: 
    print ("Aprobado!") 
else: print("Desaprobado")
