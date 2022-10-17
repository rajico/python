"""
Nombre del programa: Orden de ejecución de las estructuras alternativas
Enunciado: Realiza el ejercicio 56 (página 100) del libro "Introducción a la Programación con Python 3".
Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada uno de los siguientes casos:
1) a = 2 y b = 6. Desde la línea 12 hasta la 19, en orden.
2) a = 0 y b = 3. Desde la 12 hasta la 15, desde la 21 hasta la 23, en orden.
3) a = 0 y b = −3. Desde la 12 hasta la 15, desde la 21 hasta la 23, en orden.
4) a = 0 y b = 0. Desde la 12 hasta la 15, desde la 21, 24 y 25, en orden.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

print('Programa para la resolución de la ecuación ax+b=0.')

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))

if a != 0:
    x = -b / a
    print('Solución: ', x)

if a == 0:
    if b != 0:
        print('La ecuación no tiene solución.')
    if b == 0:
        print('La ecuación tiene infinitas soluciones.')
