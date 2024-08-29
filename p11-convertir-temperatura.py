# p11-convertir-temperatura - Convertir temperatura ºC a ºF

# Solicitar al usuario la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Calcular la temperatura en grados Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrar el resultado
print(f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f}")
