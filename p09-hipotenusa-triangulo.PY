# P09-hipotenusa-triangulo - Calculo de hipotenusa 
import math

# Solicitar al usuario las longitudes de los lados
longlado1 = float(input("Ingrese la longitud del primer lado: "))
longlado2 = float(input("Ingrese la longitud del segundo lado: "))

# Calcular la hipotenusa
hipotenusa = math.sqrt(longlado1 ** 2 + longlado2 ** 2)

# Mostrar el resultado
print(f"La hipotenusa del triángulo rectángulo es: {hipotenusa:.2f}")

