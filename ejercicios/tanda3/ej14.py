"""
Nombre del programa: Encontrar subcadena
Descripción: Realizar un programa que compruebe si una cadena contiene una subcadena.
Las dos cadenas se introducen por teclado.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 23/10/22
"""

import re

string = input('Introduce una cadena: ')
substring = input('Subcadena a buscar: ')
search = ""

for i in string:
    search = re.search(substring, string)

if search:
    print(f'Se ha encontrado la subcadena {substring} en {string}.')
else:
    print(f'No se ha encontrado la subcadena {substring} en {string}.')
