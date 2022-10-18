"""
Nombre del programa: Cuántos días tiene x mes
Enunciado: Escribe un programa que pida un número entero entre uno y doce e imprima el número
de días que tiene el mes correspondiente.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

month_num = int(input('Introduce el número del mes: '))  # Indicamos al usuario que introduzca
# el número que corresponda con un mes

january = 31  # Almacenamos el número de días que tiene enero
february = 28  # Almacenamos el número de días que tiene febrero
march = 31  # Almacenamos el número de días que tiene marzo
april = 30  # Almacenamos el número de días que tiene abril
may = 31  # Almacenamos el número de días que tiene mayo
june = 30  # Almacenamos el número de días que tiene junio
july = 31  # Almacenamos el número de días que tiene julio
august = 31  # Almacenamos el número de días que tiene agosto
september = 30  # Almacenamos el número de días que tiene septiembre
october = 31  # Almacenamos el número de días que tiene octubre
november = 30  # Almacenamos el número de días que tiene noviembre
december = 31  # Almacenamos el número de días que tiene diciembre

if 1 <= month_num <= 12:  # Si el número que corresponde al mes está comprendido entre el 1 y el 12...
    if month_num == 1:  # Si el número es 1...
        print(f'Enero tiene {january} días.')  # Mostramos el número de días que tiene enero
    elif month_num == 2:  # Si el número es 2...
        print(f'Febrero tiene {february} días, pero en años bisiestos tiene 29.')  # Mostramos el número de días
        # que tiene febrero
    elif month_num == 3:  # Si el número es 3...
        print(f'Marzo tiene {march} días.')  # Mostramos el número de días que tiene marzo
    elif month_num == 4:  # Si el número es 4...
        print(f'Abril tiene {april} días.')  # Mostramos el número de días que tiene abril
    elif month_num == 5:  # Si el número es 5...
        print(f'Mayo tiene {may} días.')  # Mostramos el número de días que tiene mayo
    elif month_num == 6:  # Si el número es 6...
        print(f'Junio tiene {june} días.')  # Mostramos el número de días que tiene junio
    elif month_num == 7:  # Si el número es 7...
        print(f'Julio tiene {july} días.')  # Mostramos el número de días que tiene julio
    elif month_num == 8:  # Si el número es 8...
        print(f'Agosto tiene {august} días.')  # Mostramos el número de días que tiene agosto
    elif month_num == 9:  # Si el número es 9...
        print(f'Septiembre tiene {september} días.')  # Mostramos el número de días que tiene septiembre
    elif month_num == 10:  # Si el número es 10...
        print(f'Octubre tiene {october} días.')  # Mostramos el número de días que tiene octubre
    elif month_num == 11:  # Si el número es 11...
        print(f'Noviembre tiene {november} días.')  # Mostramos el número de días que tiene noviembre
    elif month_num == 12:  # Si el número es 12...
        print(f'Diciembre tiene {december} días.')  # Mostramos el número de días que tiene diciembre
else:  # De lo contrario...
    print('ERROR. Número incorrecto.')  # Indicamos un error
