"""
Nombre del programa: Determinar tipo de triángulo
Enunciado: Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta lo siguiente:

    Si se cumple Pitágoras entonces es triángulo rectángulo
    Si solo dos lados del triángulo son iguales entonces es isósceles.
    Si los 3 lados son iguales entonces es equilátero.
    Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Pedimos al usuario los datos de entrada A, B y C

a = float(input('Introduce la dimensión A: '))
b = float(input('Introduce la dimensión B: '))
c = float(input('Introduce la dimensión C: '))

# Construimos la estructura alternativa

if a**2+b**2 == c**2 or b**2+c**2 == a**2 or c**2+a**2 == b**2:
    print('Triángulo rectángulo.')
if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print('Triángulo isósceles.')
else:
    if a == b and a == c:
        print('Triángulo equilátero.')
    else:
        print('Triángulo escaleno.')
