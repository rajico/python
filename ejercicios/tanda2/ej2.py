"""
Nombre del programa: Orden de ejecución de las estructuras alternativas
Enunciado: Realiza el ejercicio 56 (página 100) del libro "Introducción a la Programación con Python 3".
Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada uno de los siguientes casos:
1) a = 2 y b = 6.
2) a = 0 y b = 3.
3) a = 0 y b = −3.
4) a = 0 y b = 0.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

print('Programa para la resolución de la ecuación ax+b=0.')

a = float(input('Valor de a: '))  # Pedimos al usuario que introduzca el valor de a
b = float(input('Valor de b: '))  # Pedimos al usuario que introduzca el valor de b

if a != 0:  # Si a es diferente a 0...
    x = -b / a  # X es igual al resultado de -b / a
    print('Solución: ', x)  # Mostramos por pantalla la solución

if a == 0:  # Si a es exactamente igual a 0...
    if b != 0:  # Y además, b es diferente a 0...
        print('La ecuación no tiene solución.')  # La ecuación no se puede solucionar
    if b == 0:  # Y además, b es exactamente igual a 0...
        print('La ecuación tiene infinitas soluciones.')  # La ecuación tiene infinitas soluciones
