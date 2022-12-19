"""
Nombre del programa: MAX y MIN en arrays
Descripción: Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos
junto con las palabras “máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 12/11/22
"""

import numpy as np


def max_num_ar(arr):
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num


def min_num_ar(arr):
    min_num = arr[0]
    for i in arr:
        if i < min_num:
            min_num = i
    return min_num


array = np.array([])

for n in range(10):
    array = np.append(array, int(input("Introduce un numero: ")))
    print(f"El array tiene: {array}")
    print(f"El máximo es: {max_num_ar(array)}")
    print(f"El mínimo es: {min_num_ar(array)}")
