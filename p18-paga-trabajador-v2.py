# p18-paga-trabajador-v2 - Calcular la paga de un trabajador considerando las horas extra
print('Calculando la paga de horas extra de un trabajador (se pagan al doble)...')

nombre = input('Dame tu nombre > ')
horas = int(input('Horas trabajadas > '))
paga = int(input('Paga x hora > '))

if horas > 40:
    extra = horas - 40
    total = (40 * paga) + (extra * 2 * paga)
else:
    total = horas * paga

print(f'{nombre} trabajó {horas} horas, con una paga de {paga} por hora, total de pago {total}')
