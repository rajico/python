"""
Nombre del programa: Arrays de números enteros, al cuadrado y al cubo
Descripción: Define tres arrays de 20 números enteros cada uno, con nombres número, cuadrado y cubo.
Carga el array número con valores aleatorios entre 0 y 100.
En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el array número.
En el array cubo se deben almacenar los cubos de los valores que hay en número.
A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 12/11/22
"""

import numpy as np
import random as rd

numero = np.empty((0, 1), int)
cuadrado = np.empty((0, 1), int)
cubo = np.empty((0, 1), int)

for n in range(20):
    rand_num = rd.randrange(0, 100)
    numero = np.append(numero, rand_num)
    cuadrado = np.append(cuadrado, numero[n] ** 2)
    cubo = np.append(cubo, numero[n] ** 3)
    print(numero[n], cuadrado[n], cubo[n])
