"""
Nombre del programa:
Descripción: Realiza un programa que rellene un array de 6 filas por 10 columnas con
números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Modifica el programa anterior de tal forma que no se repita ningún número en el array.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/11/22
"""

import numpy as np
import random as rand


def min_num_ar(arr):
    min_num = arr[0][0]
    pos = ''
    for i in range(0, len(arr)):
        for x in range(0, len(arr[i])):
            if arr[i][x] < min_num:
                min_num = arr[i][x]
                pos = str(i+1)+"-"+str(x+1)
    return min_num, pos


def max_num_ar(arr):
    max_num = arr[0][0]
    pos = ''
    for i in range(0, len(arr)):
        for y in range(0, len(arr[i])):
            if arr[i][y] > max_num:
                max_num = arr[i][y]
                pos = str(i+1)+"-"+str(y+1)
    return max_num, pos


rows = 6
cols = 10
numbers = np.empty((rows, cols), int)

for row in range(0, rows):
    for col in range(0, cols):
        numbers[row][col] = rand.randint(0, 1000)
        # a falta de controlar que el número se encuentre en el array o no
        # while true: n = random.randint(0, 1000) if n not in matriz: matriz[row][col] = n break
        # Crear conjunto vacío conjunto = set() y añadir con .add el número aleatorio
        # Para controlar, usar len(conjunto) != 60: conjunto.add(random)
        # Para terminar, crear una lista con los datos del conjunto con l = lista(conjunto)

min_nums, min_pos = min_num_ar(numbers)
max_nums, max_pos = max_num_ar(numbers)

print(numbers)
print(f"El número mínimo es {min_nums}, que está en la posición {min_pos}")
print(f"El número máximo es {max_nums}, que está en la posición {max_pos}")
