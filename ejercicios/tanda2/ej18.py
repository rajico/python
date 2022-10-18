"""
Nombre del programa: Días de la semana
Enunciado: Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente.
Si introducimos otro número nos da un error.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

day = int(input('Introduce el número del día de la semana: '))  # Indicamos al usuario que introduzca
# el número que corresponda con un día de la semana

monday = 'lunes'  # Almacenamos la cadena 'lunes'
tuesday = 'martes'  # Almacenamos la cadena 'martes'
wednesday = 'miércoles'  # Almacenamos la cadena 'miércoles'
thursday = 'jueves'  # Almacenamos la cadena 'jueves'
friday = 'viernes'  # Almacenamos la cadena 'viernes'
saturday = 'sábado'  # Almacenamos la cadena 'sábado'
sunday = 'domingo'  # Almacenamos la cadena 'domingo'

if 1 <= day <= 7:  # Si el número del día está comprendido entre 1 y 7...
    if day == 1:  # Si el número es 1...
        print(f'El número corresponde al {monday}.')  # Mostramos que corresponde al lunes
    elif day == 2:  # Si el número es 2...
        print(f'El número corresponde al {tuesday}.')  # Mostramos que corresponde al martes
    elif day == 3:  # Si el número es 3...
        print(f'El número corresponde al {wednesday}.')  # Mostramos que corresponde al miércoles
    elif day == 4:  # Si el número es 4...
        print(f'El número corresponde al {thursday}.')  # Mostramos que corresponde al jueves
    elif day == 5:  # Si el número es 5...
        print(f'El número corresponde al {friday}.')  # Mostramos que corresponde al viernes
    elif day == 6:  # Si el número es 6...
        print(f'El número corresponde al {saturday}.')  # Mostramos que corresponde al sábado
    elif day == 7:  # Si el número es 7...
        print(f'El número corresponde al {sunday}.')  # Mostramos que corresponde al domingo
else:  # De lo contrario...
    print('ERROR. Número incorrecto.')  # Indicamos un error
