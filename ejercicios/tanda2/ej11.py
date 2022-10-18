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

a = float(input('Introduce la dimensión A: '))  # Pedimos al usuario que introduzca la dimensión A
b = float(input('Introduce la dimensión B: '))  # Pedimos al usuario que introduzca la dimensión B
c = float(input('Introduce la dimensión C: '))  # Pedimos al usuario que introduzca la dimensión C

if a**2+b**2 == c**2 or b**2+c**2 == a**2 or c**2+a**2 == b**2:  # Si se cumple Pitágoras...
    print('Triángulo rectángulo.')  # Indicamos que se trata de un triángulo rectángulo
if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):  # Si solo dos lados del
    # triángulo son iguales...
    print('Triángulo isósceles.')  # Indicamos que se trata de un triángulo isósceles
else:  # De lo contrario...
    if a == b and a == c:  # Si los 3 lados son iguales...
        print('Triángulo equilátero.')  # Indicamos que se trata de un triángulo equilátero
    else:  # De lo contrario...
        print('Triángulo escaleno.')  # Indicamos que se trata de un triángulo escaleno
