# Descripción: Realiza un programa que reciba una cantidad de minutos y muestre
# por pantalla a cuantas horas y minutos corresponde.
# Autor del ejercicio: Rafael Jiménez Cobos

total_minutes = int(input('Introduce una cantidad de minutos: '))

hour = total_minutes // 60
minutes = total_minutes % 60

print(f'El tiempo resultante es {hour:02}:{minutes:02}')
