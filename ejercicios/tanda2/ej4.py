"""
Nombre del programa: División de números con aviso por 0
Enunciado: Crea un programa que pida al usuario dos números y muestre su división
si el segundo no es cero, o un mensaje de aviso en caso contrario.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Preguntamos al usuario dos números que recogeremos en las variables num1 y num2

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

# Creamos la estructura alternativa con if else para realizar y mostrar la división, y en caso
# de que el segundo número sea un 0, un aviso.

if num2 > 0:
    div = num1 // num2
    print(f'El resultado de la división entre {num1} y {num2} es {div}.')
else:
    print(f'¡AVISO! No puedes dividir entre 0.')
