"""
Nombre del programa: El mayor entre 5 números
Enunciado: Realiza un programa que pida cinco números enteros y diga cuál es el mayor.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

num1 = int(input('Introduce el primer número: '))  # Indicamos al usuario introducir el primer número
num2 = int(input('Introduce el segundo número: '))  # Indicamos al usuario introducir el segundo número
num3 = int(input('Introduce el tercero número: '))  # Indicamos al usuario introducir el tercer número
num4 = int(input('Introduce el cuarto número: '))  # Indicamos al usuario introducir el cuarto número
num5 = int(input('Introduce el quinto número: '))  # Indicamos al usuario introducir el quinto número

if num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5:  # Si el primer número es mayor...
    print(f'{num1} es mayor que {num2}, {num3}, {num4} y {num5}.')  # Lo indicamos
elif num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:  # Si el segundo número es mayor...
    print(f'{num2} es mayor que {num1}, {num3}, {num4} y {num5}.')  # Lo indicamos
elif num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:  # Si el tercer número es mayor...
    print(f'{num3} es mayor que {num1}, {num2}, {num4} y {num5}.')  # Lo indicamos
elif num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:  # Si el cuarto número es mayor...
    print(f'{num4} es mayor que {num1}, {num2}, {num3} y {num5}.')  # Lo indicamos
else:  # De lo contrario...
    print(f'{num5} es mayor que {num1}, {num2}, {num3} y {num4}.')  # Indicamos que el quinto número es
    # el mayor
