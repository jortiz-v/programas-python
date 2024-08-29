# p13-calculo-tiempo - Convertir horas a días, minutos y segundos

# Solicitar al usuario la cantidad de horas
horas = float(input("Ingrese la cantidad de horas: "))

# Calcular los días, minutos y segundos equivalentes
dias = horas // 24  # División entera para obtener los días completos
horas_restantes = horas % 24  # Horas que sobran después de calcular los días

minutos = horas_restantes * 60  # Convertir las horas restantes a minutos
segundos = minutos * 60  # Convertir minutos a segundos

# Mostrar los resultados
print(f"{horas} horas equivalen a:")
print(f"{int(dias)} días")
print(f"{int(minutos)} minutos")
print(f"{int(segundos)} segundos")
