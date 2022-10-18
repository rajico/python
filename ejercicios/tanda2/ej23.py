"""
Nombre del programa: Número más cercano al primero introducido
Enunciado: Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos
números es más cercano al primero. Por ejemplo, si el usuario introduce los
números 2, 6, 4, 1 y 10, el programa responderá que el número más cercano al 2 es el 1.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

num1 = int(input('Introduce el primer número: '))  # Indicamos al usuario introducir el primer número
num2 = int(input('Introduce el segundo número: '))  # Indicamos al usuario introducir el segundo número
num3 = int(input('Introduce el tercero número: '))  # Indicamos al usuario introducir el tercer número
num4 = int(input('Introduce el cuarto número: '))  # Indicamos al usuario introducir el cuarto número
num5 = int(input('Introduce el quinto número: '))  # Indicamos al usuario introducir el quinto número

if abs(num1 - num2) < abs(num1 - num3):  # Si la diferencia entre el primer y el segundo número es menor
    # que la diferencia entre el primer y el tercer número...
    close_to_num1 = num2  # El número más cercano es el segundo
else:  # De lo contrario...
    close_to_num1 = num3  # El número más cercano es el tercero
if abs(num1 - num4) < abs(num1 - close_to_num1):  # Si la diferencia entre el primer y el cuarto número es menor
    # que la diferencia entre el primer y el quinto número...
    close_to_num1 = num4  # El número más cercano es el cuarto
if abs(num1 - num5) < abs(num1 - close_to_num1):  # Si la diferencia entre el primer y el quinto número es menor
    # que la diferencia entre el primer número y el más cercano a este...
    close_to_num1 = num5  # El número más cercano es el quinto

print(f'El número más cercano a {num1} es {close_to_num1}.')  # Mostramos el número más cercano al primero
