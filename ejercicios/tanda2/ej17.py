"""
Nombre del programa: Caras de un dado
Enunciado: Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar
un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara
opuesta al resultado obtenido.

    Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
    Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el
    mensaje: “ERROR: número incorrecto.”.

Ejemplo:

Introduzca número del dado: 5
En la cara opuesta está el "dos".

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

dice = int(input('Introduce el número del dado: '))

one = 'uno'
two = 'dos'
three = 'tres'
four = 'cuatro'
five = 'cinco'
six = 'seis'

if 1 <= dice <= 6:
    if dice == 1:
        print(f'En la cara opuesta está el {six}')
    elif dice == 2:
        print(f'En la cara opuesta está el {five}')
    elif dice == 3:
        print(f'En la cara opuesta está el {four}')
    elif dice == 4:
        print(f'En la cara opuesta está el {three}')
    elif dice == 5:
        print(f'En la cara opuesta está el {two}')
    elif dice == 6:
        print(f'En la cara opuesta está el {one}')
else:
    print('ERROR. Número incorrecto.')
