"""
Nombre del programa: Trabajando con intervalos
Descripción: Escribe un programa que pida el límite inferior y superior de un intervalo.
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:

    La suma de los números que están dentro del intervalo (intervalo abierto).
    Cuantos números están fuera del intervalo.
    Informa si hemos introducido algún número igual a los límites del intervalo.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/10/22
"""

lower_limit = int(input('Introduce el límite inferior del intervalo: '))
upper_limit = int(input('Introduce el límite superior del intervalo: '))
add_numbers = 0
numbers_outside = 0

while lower_limit > upper_limit:
    print('¡ERROR! El intervalo inferior es mayor al superior, introduce los valores de nuevo.')
    lower_limit = int(input('Introduce el límite inferior del intervalo: '))
    upper_limit = int(input('Introduce el límite superior del intervalo: '))

num = int(input('Introduce un número: '))

while num != 0:
    if lower_limit < num < upper_limit:
        add_numbers += num
    elif num <= lower_limit or num >= upper_limit:
        numbers_outside += 1
    num = int(input('Introduce un número: '))

print(f'Suma de los números entre {lower_limit} y {upper_limit}: {add_numbers}.')
print(f'Números fuera del intervalo: {numbers_outside}')

if num == lower_limit:
    print('El número introducido es igual al límite inferior.')
elif num == upper_limit:
    print('El número introducido es igual al límite superior.')
