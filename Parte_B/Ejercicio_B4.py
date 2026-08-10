puntajes_B3= [120,45,300,80,120]
puntajes_ALtos=[]
for puntaje in puntajes_B3: 
    if puntaje >100: 
        puntajes_ALtos.append(puntaje)
print (f"lista original intacta{puntajes_B3}")
print (f"lista con valores mayores a 100: {puntajes_ALtos}")