"""
Nombre del programa: ¿Cadena mayúscula?
Enunciado: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

text = input('Introduce una cadena: ')  # Pedimos al usuario que introduzca un valor de tipo cadena

if any(c.isupper() for c in text):  # Si en la cadena encontramos alguna letra en mayúscula...
    print('La cadena contiene como mínimo un carácter en mayúscula.')  # Lo indicamos en pantalla
else:  # De lo contrario...
    print('La cadena no contiene mayúsculas.')  # Lo indicamos en pantalla
