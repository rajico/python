"""
Nombre del programa: Cuántos días tiene x mes
Enunciado: Escribe un programa que pida un número entero entre uno y doce e imprima el número
de días que tiene el mes correspondiente.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

month_num = int(input('Introduce el número del mes: '))

january = 31
february = 28
march = 31
april = 30
may = 31
june = 30
july = 31
august = 31
september = 30
october = 31
november = 30
december = 31

if 1 <= month_num <= 12:
    if month_num == 1:
        print(f'Enero tiene {january} días.')
    elif month_num == 2:
        print(f'Febrero tiene {february} días, pero en años bisiestos tiene 29.')
    elif month_num == 3:
        print(f'Marzo tiene {march} días.')
    elif month_num == 4:
        print(f'Abril tiene {april} días.')
    elif month_num == 5:
        print(f'Mayo tiene {may} días.')
    elif month_num == 6:
        print(f'Junio tiene {june} días.')
    elif month_num == 7:
        print(f'Julio tiene {july} días.')
    elif month_num == 8:
        print(f'Agosto tiene {august} días.')
    elif month_num == 9:
        print(f'Septiembre tiene {september} días.')
    elif month_num == 10:
        print(f'Octubre tiene {october} días.')
    elif month_num == 11:
        print(f'Noviembre tiene {november} días.')
    elif month_num == 12:
        print(f'Diciembre tiene {december} días.')
else:
    print('ERROR. Número incorrecto.')
