"""
Nombre del programa: El mayor entre 3 números
Enunciado: Realiza un programa que pida tres números enteros y diga cuál es el mayor.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercero número: '))

if num1 > num2 and num1 > num3:
    print(f'{num1} es mayor que {num2} y {num3}.')
elif num2 > num1 and num2 > num3:
    print(f'{num2} es mayor que {num1} y {num3}.')
else:
    print(f'{num3} es mayor que {num1} y {num2}.')
