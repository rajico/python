"""
Nombre del programa: Cronómetro
Descripción: Hacer un programa que muestre un cronómetro, indicando las horas, minutos y segundos.
Para hacer una espera en Python podemos usar el método sleep del módulo time.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 22/10/22
"""

import time

print('--- CRONOMETRO ---')

for hours in range(0, 24):
    for minutes in range(0, 60):
        for seconds in range(0, 60):
            print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')
            time.sleep(1)
