"""
Nombre del programa: Número mayor o menor
Enunciado: Programa que pida dos números e indique si el primero es mayor que el segundo o no.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Pedimos al usuario que introduzca dos números, los almacenamos en las variables num1 y num2

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

# Creamos la estructura alternativa con if else

if num1 > num2:
    print(f'{num1} es mayor que {num2}.')
else:
    print(f'{num1} es menor que {num2}.')
