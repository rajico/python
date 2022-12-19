"""
Nombre del programa: Cálculos con números aleatorios
Descripción: Programa que genera números aleatorios para luego realizar cálculos con ellos. Se le pide al usuario
el número inicial y el número final del rango para la generación de los números aleatorios.

Calcular la media muestral, la mediana, el error medio, la desviación estándar muestral y el rango.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 25/10/22
"""

import random
import sys

try:
    # Supongamos que necesitamos que se generen 10 números aleatorios
    MIN_RANGE = 0
    MAX_RANGE = 10

    range_init_num = float(input('Inserta el número inicial para el rango: '))
    range_end_num = float(input('Inserta el número final para el rango: '))

    num_list = []
    error = 0
    mean_calc = 0

    print('\n--- Estos son los números generados aleatoriamente --- \n')

    for num in range(MIN_RANGE, MAX_RANGE):
        random_numbers = random.uniform(range_init_num, range_end_num)
        num_list.append(random_numbers)
        mean_calc += random_numbers
        print(f'Número {num}: {num_list[num]}')

    print('\n--- Vamos a realizar los cálculos necesarios --- \n')

    # Media muestral, sumar cada elemento y dividir entre el número de elementos total
    mean_calc = mean_calc / len(num_list)
    print(f'Media muestral: {mean_calc:.2f}')
    # Mediana, si es par, la media de los dos, si no, el elemento en medio de la lista
    if len(num_list) % 2 == 0:
        median1 = num_list[len(num_list)//2]
        median2 = num_list[len(num_list)//2 - 1]
        print(f'Mediana: {(median1 + median2)/2:.2f}')
    else:
        print(f'Mediana: {num_list[len(num_list)//2]:.2f}')
    # Error medio, diferencia de cada elemento - la media, elevando el resultado al cuadrado
    for i in range(10):
        error += abs(num_list[i])
    error = error / 10
    print(f'Error: {error:.2f}')
    # Desviación estándar muestral, sumar la diferencia al cuadrado de cada elemento menos la media
    standard_deviation_calc = sum((i-mean_calc)**2 for i in num_list) / len(num_list)
    standard_deviation = standard_deviation_calc**0.5
    print(f'Desviación estándar muestral: {standard_deviation:.2f}')
    # Rango: La diferencia entre el mayor y el menor número
    sorted_list = sorted(num_list)
    print(f'Rango: {sorted_list[-1] - sorted_list[0]:.2f}')
except ValueError:
    print('\n¡ERROR! Debes introducir números reales, separando los decimales con punto', sys.stderr)
