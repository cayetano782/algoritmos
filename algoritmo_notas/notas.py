nota = float(input("Introduce la nota (de 0 a 10): "))

if nota < 5:
    resultado = "Insuficiente"

elif nota >= 5 and nota < 7:
    resultado = "Suficiente"

elif nota >= 7 and nota < 9:
    resultado = "Notable"

elif nota >= 9 and nota <= 10:
    resultado = "Sobresaliente"

print("Tu clasificación es:")
print(resultado)