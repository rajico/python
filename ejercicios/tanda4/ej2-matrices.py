"""
Nombre del programa: Sumar arrays de dos dimensiones con números aleatorios
Descripción: Modifica el programa anterior de tal forma que los números que se introducen en el
array se generen de forma aleatoria (valores entre 100 y 999).
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/11/22
"""

import numpy as np

row_number = 4
col_number = 5
num_arr = np.empty((row_number+1, col_number+1), int)
row_col_sum = 0

for row in range(0, row_number):
    for col in range(0, col_number):
        num_arr[row][col] = np.random.randint(100, 999)

for row in range(0, row_number):
    row_sum = 0
    for col in range(0, col_number):
        row_sum += num_arr[row][col]
    num_arr[row][col_number] = row_sum
    row_col_sum += row_sum

for col in range(0, col_number):
    col_sum = 0
    for row in range(0, row_number):
        col_sum += num_arr[row][col]
    num_arr[row_number][col] = col_sum
    row_col_sum += col_sum

num_arr[row_number][col_number] = row_col_sum

for row in num_arr:
    print(str(row))
