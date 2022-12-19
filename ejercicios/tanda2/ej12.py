"""
Nombre del programa: ¿Año bisiesto?
Enunciado: Escribir un programa que lea un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es
divisible por 100, excepto que también sea divisible por 400.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

year = int(input('Introduce un año: '))

if year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0):
    print(f'El año {year} es bisiesto.')
else:
    print(f'El año {year} no es bisiesto.')
