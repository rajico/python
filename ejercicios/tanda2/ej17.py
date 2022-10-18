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

dice = int(input('Introduce el número del dado: '))  # Indicamos al usuario introducir un número que corresponda
# con la cara de un dado

one = 'uno'  # Almacenamos la cadena 'uno'
two = 'dos'  # Almacenamos la cadena 'dos'
three = 'tres'  # Almacenamos la cadena 'tres'
four = 'cuatro'  # Almacenamos la cadena 'cuatro'
five = 'cinco'  # Almacenamos la cadena 'cinco'
six = 'seis'  # Almacenamos la cadena 'seis'

if 1 <= dice <= 6:  # Si el número está entre 1 y 6...
    if dice == 1:  # Si el número es 1...
        print(f'En la cara opuesta está el {six}')  # Mostramos el número opuesto
    elif dice == 2:  # Si el número es 2...
        print(f'En la cara opuesta está el {five}')  # Mostramos el número opuesto
    elif dice == 3:  # Si el número es 3...
        print(f'En la cara opuesta está el {four}')  # Mostramos el número opuesto
    elif dice == 4:  # Si el número es 4...
        print(f'En la cara opuesta está el {three}')  # Mostramos el número opuesto
    elif dice == 5:  # Si el número es 5...
        print(f'En la cara opuesta está el {two}')  # Mostramos el número opuesto
    elif dice == 6:  # Si el número es 6...
        print(f'En la cara opuesta está el {one}')  # Mostramos el número opuesto
else:  # De lo contrario...
    print('ERROR. Número incorrecto.')  # Indicamos que el número es incorrecto
