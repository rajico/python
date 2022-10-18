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

import math  # Importamos la librería math

x1 = int(input('Introduce el punto x1: '))  # Pedimos al usuario introducir el valor del punto x1
y1 = int(input('Introduce el punto y1: '))  # Pedimos al usuario introducir el valor del punto y1
r1 = int(input('Introduce el primer radio: '))  # Pedimos al usuario introducir el valor del primer radio
x2 = int(input('Introduce el punto x2: '))  # Pedimos al usuario introducir el valor del punto x2
y2 = int(input('Introduce el punto y2: '))  # Pedimos al usuario introducir el valor del punto y2
r2 = int(input('Introduce el segundo radio: '))  # Pedimos al usuario introducir el valor del primer radio

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)  # Calculamos la distancia entre los centros

if distance > (r1 + r2):  # Si la distancia es mayor a la suma de los radios...
    print('Circunferencias exteriores.')  # Indicamos que se trata de circunferencias exteriores
elif distance == (r1 + r2):  # Si la distancia es exactamente igual a la suma de los radios...
    print('Circunferencias tangentes exteriores.')  # Indicamos que se trata de circunferencias tangentes exteriores
elif (r1 + r2) > distance > abs(r1 - r2):  # Si la distancia es menor que la suma de
    # los radios y mayor que su diferencia...
    print('Circunferencias secantes')  # Indicamos que se trata de circunferencias secantes
elif distance == abs(r1-r2):  # Si la distancia es exactamente igual a la diferencia entre los radios...
    print('Circunferencias tangentes interiores')  # Indicamos que se trata de circunferencias tangentes interiores
elif 0 < distance < abs(r1 - r2):  # Si la distancia es menor que la diferencia entre los radios y mayor que 0...
    print('Circunferencias interiores.')  # Indicamos que se trata de circunferencias interiores
elif distance == 0:  # Si la distancia es exactamente igual a 0...
    print('Circunferencias concéntricas.')  # Indicamos que se trata de circunferencias concéntricas
