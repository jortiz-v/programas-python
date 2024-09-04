# p27-calculo-notas - Calcular promedio de notas

# Solicitar las 5 calificaciones al usuario en una sola instrucción, separadas por espacios
notas = input("Ingrese las cinco calificaciones separadas por un espacio: ")

# Dividir las calificaciones ingresadas y convertirlas a flotantes
nota1, nota2, nota3, nota4, nota5 = map(float, notas.split())

# Calcular el promedio
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

# Evaluar el promedio
if promedio > 0 and promedio < 6:
    print("Quedas reprobado")
elif promedio >= 6 and promedio < 7:
    print("Pasas de panzazo")
elif promedio >= 7 and promedio < 8:
    print("Muy bien, puedes mejorar")
elif promedio >= 8 and promedio < 9:
    print("Excelente, sigue así")
elif promedio >= 9 and promedio <= 10:
    print("Perfecto, tu esfuerzo valió la pena")
else:
    print("Promedio fuera de rango")
