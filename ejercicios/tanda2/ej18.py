"""
Nombre del programa: Días de la semana
Enunciado: Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

day = int(input('Introduce el número del día de la semana: '))

monday = 'lunes'
tuesday = 'martes'
wednesday = 'miércoles'
thursday = 'jueves'
friday = 'viernes'
saturday = 'sábado'
sunday = 'domingo'

if 1 <= day <= 7:
    if day == 1:
        print(f'El número corresponde al {monday}.')
    elif day == 2:
        print(f'El número corresponde al {tuesday}.')
    elif day == 3:
        print(f'El número corresponde al {wednesday}.')
    elif day == 4:
        print(f'El número corresponde al {thursday}.')
    elif day == 5:
        print(f'El número corresponde al {friday}.')
    elif day == 6:
        print(f'El número corresponde al {saturday}.')
    elif day == 7:
        print(f'El número corresponde al {sunday}.')
else:
    print('ERROR. Número incorrecto.')
