"""
Nombre del programa: Número mayor o menor
Enunciado: Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

num1 = int(input('Introduce el primer número: '))  # Pedimos al usuario que indique el primer número
num2 = int(input('Introduce el segundo número: '))  # Pedimos al usuario que indique el segundo número

if num1 > num2:  # Si el primer número es mayor que el segundo...
    print(f'{num1} es mayor que {num2}.')  # El programa lo indica
else:  # De lo contrario...
    print(f'{num1} es menor que {num2}.')  # El programa indica que el primer número es menor
