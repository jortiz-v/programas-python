# p28-aceptar-estudiante-v2 - Decidir si un estudiante es aceptado

# Solicitar información del estudiante
nombre = input("Ingrese el nombre del estudiante: ")
sexo = input("Ingrese el sexo del estudiante (h/m): ")
edad = int(input("Ingrese la edad del estudiante: "))

# Solicitar las tres calificaciones en una sola instrucción, separadas por espacios
calificaciones = input("Ingrese las tres calificaciones separadas por un espacio: ")

# Dividir las calificaciones ingresadas y convertirlas a flotantes
nota1, nota2, nota3 = map(float, calificaciones.split())

# Calcular el promedio de calificaciones
promedio = (nota1 + nota2 + nota3) / 3

# Verificar las condiciones de aceptación
if sexo.lower() == 'm':
    if edad > 21:
        if promedio >= 8 and promedio <= 9.5:
            print(f"{nombre}, has sido aceptada, tu edad de {edad} y tus calificaciones {nota1}, {nota2} y {nota3} lo permiten.")
        else:
            print(f"{nombre}, eres mujer, tienes la edad, pero tu promedio no alcanza solo promedios de 8 a 9.5")
    else:
        print(f"{nombre}, eres mujer, pero no tienes la edad, solo mayores a 21")
else:
    print(f"{nombre}, solo aceptamos mujeres")
