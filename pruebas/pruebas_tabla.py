"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 24/11/22
"""

import random as rand
import numpy as np

array = np.empty((5, 5), int)

for x in range(0, 5):
    for y in range(0, 5):
        num = rand.randrange(0, 100)
        if num not in array:
            array[x][y] = num
        else:
            continue

"""
print('-----')
print(f'|{array} |')
print('-----')
"""

print('-----------------')
print(f'{array}')
print('-----------------')
