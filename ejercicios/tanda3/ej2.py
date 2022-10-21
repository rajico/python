"""
Nombre del programa: Trabajando con el 0
Descripción: Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir).
El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/10/22

Estructura

1) Introducimos la cantidad de números a introducir (fin del rango)
2) Se pide dicha cantidad de números
3) Mientras se ejecute el programa y se introduzcan números, se comparan con 0 y se suman a un contador
"""

import sys

try:
    num_quantity = int(input('¿Cuántos números quieres introducir? '))
    greater_than_zero = 0
    lower_than_zero = 0
    equal_to_zero = 0

    for i in range(1, num_quantity + 1):
        num = int(input('Introduce un número: '))
        if num > 0:
            greater_than_zero += 1
        if num < 0:
            lower_than_zero += 1
        if num == 0:
            equal_to_zero += 1

    if greater_than_zero != 0:
        print(f'Cantidad de números introducidos mayores que 0: {greater_than_zero}')
    if lower_than_zero != 0:
        print(f'Cantidad de números introducidos menores que 0: {lower_than_zero}')
    if equal_to_zero != 0:
        print(f'Cantidad de números iguales a 0: {equal_to_zero}')
except ValueError:
    print('¡ERROR! Debes introducir un número entero.', file=sys.stderr)
