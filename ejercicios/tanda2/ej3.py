"""
Nombre del programa: Número par o impar
Enunciado: Escribe un programa que lea un número e indique si es par o impar.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

num = int(input('Introduce un número: '))  # Primero, pedimos un número al usuario:

# Creamos la estructura alternativa con if else y comprobamos si el número es par o no si
# al dividir entre 2 nos devuelve 0.

if num % 2 == 0:  # Si el resto de la división entre el número introducido y 2 es exactamente igual a 0...
    print(f'El número {num} es par.')  # El número es par
else:  # De lo contrario...
    print(f'El número {num} es impar.')  # El número es impar
