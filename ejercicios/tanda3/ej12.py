"""
Nombre del programa: Sustituir caracteres
Descripción: Pide una cadena y dos caracteres por teclado (valida que sea un carácter)
sustituye la aparición del primer carácter en la cadena por el segundo carácter.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 23/10/22
"""

string = input('Introduce una cadena: ')
char1 = input('Introduce el primer carácter: ')
char2 = input('Introduce el segundo carácter: ')
new_string = ""
pos = 0

for i in range(pos < 0, len(string)-1):
    if char1 in string:
        new_string = string.replace(char1, char2, )

if char1 not in string:
    print(f'El carácter {char1} no se encuentra en {string}, introduce otro carácter.')

print(new_string)
