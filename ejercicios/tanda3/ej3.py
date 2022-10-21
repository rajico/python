"""
Nombre del programa: VOCAL o NO VOCAL
Descripción: Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario
el programa termina cuando se introduce un espacio.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/10/22

Estructura

1) Pedimos por pantalla una letra
2) Comparamos si la letra es vocal o no vocal o si es un espacio en blanco
3) Si es vocal, se imprime por pantalla VOCAL
4) Si es una consonante, se imprime por pantalla NO VOCAL
5) Por último, si es un espacio en blanco, termina el programa
"""

import re

string = input('Introduce un carácter: ')

if len(string) == 1:
    while string != ' ':
        if re.search("[aeiouAEIOU]", string) or re.search("[áéíóúÁÉÍÓÚ]", string):
            print(f'{string} es VOCAL.')
        elif re.search("[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]", string):
            print(f'{string} es NO VOCAL.')
        else:
            if re.search("[0-9]", string):
                print(f'{string} es un número, por favor, introduce un carácter de tipo texto.')
            if re.search("[.,;:-_()\'\"?¿¡!]", string):
                print(f'{string} es un carácter de puntuación, por favor, introduce un carácter de tipo texto.')
        string = input('Introduce un carácter: ')
else:
    print('Debes introducir un solo carácter.')
