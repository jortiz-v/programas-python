# p23-numeros-consecutivos - Verificar si tres números son consecutivos

# Solicitar al usuario que ingrese tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar si los números son consecutivos
if num2 == num1 + 1 and num3 == num2 + 1:
    print("Los números son consecutivos.")
else:
    print("Los números no son consecutivos.")
