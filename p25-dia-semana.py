# p25-dia-semana - Mostrar el día de la semana

# Solicitar al usuario un número del 1 al 7
num = int(input("Ingrese un número entre 1 y 7: "))

# Mostrar el día correspondiente
if num == 1:
    print("Domingo")
elif num == 2:
    print("Lunes")
elif num == 3:
    print("Martes")
elif num == 4:
    print("Miércoles")
elif num == 5:
    print("Jueves")
elif num == 6:
    print("Viernes")
elif num == 7:
    print("Sábado")
else:
    print("Número inválido")
