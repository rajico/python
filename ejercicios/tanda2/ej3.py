"""
Nombre del programa: Número par o impar
Enunciado: Escribe un programa que lea un número e indique si es par o impar.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Primero, pedimos un número al usuario:

num = int(input('Introduce un número: '))

# Creamos la estructura alternativa con if else y comprobamos si el número es par o no si
# al dividir entre 2 nos devuelve 0.

if num % 2 == 0:
    print(f'El número {num} es par.')
else:
    print(f'El número {num} es impar.')
