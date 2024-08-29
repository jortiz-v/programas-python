# p12-volumen-cilindro - Calcular el volumen de un cilindro

import math

# Solicitar al usuario el radio y la altura del cilindro
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular el volumen del cilindro
volumen = math.pi * (radio ** 2) * altura

# Mostrar el resultado
print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas")
