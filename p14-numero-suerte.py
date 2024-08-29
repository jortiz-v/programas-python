# p14-numero-suerte - Calcular el número de la suerte a partir del año de nacimiento

# Solicitar al usuario el año de nacimiento
ano_nacimiento = input("Ingrese su año de nacimiento: ")

# Mostrar los dígitos individuales
print(f"Los dígitos individuales del año {ano_nacimiento} son: ", end="")

# Inicializar la suma para el número de la suerte
numero_suerte = 0

# Calcular la suma de los dígitos individuales
for digito in ano_nacimiento:
    print(digito, end=" ")
    numero_suerte += int(digito)

# Mostrar el número de la suerte
print(f"\nEl número de la suerte es: {numero_suerte}")
