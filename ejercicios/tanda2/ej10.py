"""
Nombre del programa: Clasificador de circunferencias
Enunciado: Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de
dos circunferencias y las clasifique en uno de estos estados:

    exteriores
    tangentes exteriores
    secantes
    tangentes interiores
    interiores
    concéntricas

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

import math

x1 = int(input('Introduce el punto x1: '))
y1 = int(input('Introduce el punto y1: '))
r1 = int(input('Introduce el primer radio: '))
x2 = int(input('Introduce el punto x2: '))
y2 = int(input('Introduce el punto y2: '))
r2 = int(input('Introduce el segundo radio: '))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

if distance > (r1 + r2):
    print('Circunferencias exteriores.')
elif distance == (r1 + r2):
    print('Circunferencias tangentes exteriores.')
elif (r1 + r2) > distance > abs(r1 - r2):
    print('Circunferencias secantes')
elif distance == abs(r1-r2):
    print('Circunferencias tangentes interiores')
elif 0 < distance < abs(r1 - r2):
    print('Circunferencias interiores.')
elif distance == 0:
    print('Circunferencias concéntricas.')
else:
    print('No se han encontrado relación entre las circunferencias.')
