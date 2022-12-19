"""
Nombre del programa: Contar cadenas
Descripción: Suponiendo que hemos introducido una cadena por teclado que representa una frase
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 23/10/22
"""

string = input('Introduce una frase: ')
counter = 0

for i in string:
    counter = len(string.split())

print(f'{string} tiene {counter} palabras.')
