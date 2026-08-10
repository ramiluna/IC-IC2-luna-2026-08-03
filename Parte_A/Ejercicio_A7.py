# 1. Aca defino un valor de entrada .
kilometros = 10 

# 2. Factores de conversión fijos
factor_km_a_millas = 0.621371
factor_millas_a_pies = 5280

# 3. La cadena de conversiones (de acuerdo al valor de KM que se decida poner en el punto 1)
millas = kilometros * factor_km_a_millas
pies = millas * factor_millas_a_pies

# 4. camino completo, con 2 decimales)
print(f"{kilometros} km  →  {millas:.2f} millas  →  {pies:.2f} pies")