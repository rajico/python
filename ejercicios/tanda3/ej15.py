"""
Nombre del programa: Palíndromos
Descripción: Introducir una cadena de caracteres e indicar si es un palíndromo.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 23/10/22
"""

string1 = input('Introduce una cadena: ')
string2 = ""
pos = 0

for i in range(len(string1)-1, pos, -1):
    string2 = string1[::-1]

if string1 == string2:
    print('Es un palíndromo.')
else:
    print('No es palíndromo.')
