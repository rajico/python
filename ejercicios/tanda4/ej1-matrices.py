"""
Nombre del programa: Sumar arrays de dos dimensiones
Descripción: Escribe un programa que pida 20 números enteros.
Estos números se deben introducir en un array de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/11/22
"""

import numpy as np

"""
Inicializamos las variables row_number y col_number para almacenar el número de filas y columnas.
Creamos el array vacío.
Almacenamos en row_col_sum la suma TOTAL.
"""

row_number = 4
col_number = 5
num_arr = np.empty((row_number+1, col_number+1), int)
row_col_sum = 0

"""
Hacemos dos bucles, uno para las filas, y otro para las columnas. Insertamos tantos números en el array
como filas y columnas haya.
"""

for row in range(0, row_number):
    for col in range(0, col_number):
        num_arr[row][col] = int(input('Introduce un número: '))

"""
En los siguientes bucles, calculamos la suma de las filas, y se la asignamos a la última fila del array.
Por último, sumamos el resultado de la suma de filas a la suma total.
"""

for row in range(0, row_number):
    row_sum = 0
    for col in range(0, col_number):
        row_sum += num_arr[row][col]
    num_arr[row][col_number] = row_sum
    row_col_sum += row_sum

"""
En los siguientes bucles, calculamos la suma de las columnas, y se la asignamos a la última columna del array.
Por último, sumamos el resultado de la suma de columnas a la suma total.
"""

for col in range(0, col_number):
    col_sum = 0
    for row in range(0, row_number):
        col_sum += num_arr[row][col]
    num_arr[row_number][col] = col_sum
    row_col_sum += col_sum

"""
Asignamos la suma total a la última posición del array.
"""

num_arr[row_number][col_number] = row_col_sum

"""
Para finalizar, mostramos el array.
"""

for row in num_arr:
    print(str(row))
