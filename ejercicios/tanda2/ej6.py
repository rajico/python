"""
Nombre del programa: ¿Cadena mayúscula?
Enunciado: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Pedimos al usuario que introduzca un valor de tipo cadena.

text = input('Introduce una cadena: ')

# Creamos la estructura alternativa con if else y comprobamos si la cadena posee una letra mayúscula.

if any(c.isupper() for c in text):
    print('La cadena contiene como mínimo un carácter en mayúscula.')
else:
    print('La cadena no contiene mayúsculas.')
