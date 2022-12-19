"""
Nombre del programa: Diagrama de temperatura media
Descripción: Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año
y que muestre a continuación un diagrama de barras horizontales con esos datos.
Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 12/11/22
"""

import numpy as np

temperaturas = np.array([])

mapa_temperaturas = {}

for n in range(1, 13):
    temperaturas = np.append(temperaturas, float(input(f"Introduce la temperatura media del mes {n}: ")))

for tmp in temperaturas:
    if tmp in mapa_temperaturas:
        mapa_temperaturas[tmp] += 1
    else:
        mapa_temperaturas[tmp] = 1

for valor in sorted(mapa_temperaturas):
    print(f'{valor}: {"*" * mapa_temperaturas[valor]}')
