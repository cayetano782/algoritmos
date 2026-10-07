def puede_votar(edad):
    resultado = (edad >= 18) and (edad < 120)
    return resultado

# Llamadas de prueba
print(puede_votar(15))   # False (menor de 18)
print(puede_votar(20))   # True (puede votar)
print(puede_votar(125))  # False (mayor o igual a 120)