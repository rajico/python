"""
Nombre del programa: ¿Cadena mayúscula?
Enunciado: Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

text = input('Introduce una cadena: ')

if len(text) == 1:
    if text.isupper():
        print(f'La cadena {text} está en mayúscula.')
    else:
        print(f'La cadena {text} no está en mayúscula.')
else:
    print('Debes introducir una letra.')

"""
Con un solo if

if len(text) == 1 and text.isupper()
"""
