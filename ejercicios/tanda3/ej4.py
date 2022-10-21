"""
Nombre del programa: Imprimir números pares
Descripción: Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/10/22
"""

INIT_RANGE_NUM = 0
END_RANGE_NUM = 0

num1 = int(input('Introduce el primer número par: '))
num2 = int(input('Introduce el segundo número par: '))

if num1 > num2:
    INIT_RANGE_NUM = num2
    END_RANGE_NUM = num1
elif num1 <= num2:
    INIT_RANGE_NUM = num1
    END_RANGE_NUM = num2

for i in range(INIT_RANGE_NUM+1, END_RANGE_NUM):
    if i % 2 == 0:
        print(i)
