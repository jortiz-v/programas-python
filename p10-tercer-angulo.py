# p10-tercer-angulo - Calculo del tercer Angulo

# Solicitar al usuario los dos ángulos del triángulo
angulo1 = float(input("Ingrese el primer ángulo del triángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo del triángulo: "))

# Calcular el tercer ángulo
angulo3 = 180 - (angulo1 + angulo2)

# Mostrar el resultado
print(f"El tercer ángulo del triángulo es: {angulo3:.2f} grados")
