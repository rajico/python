"""
Nombre del programa: Contar mayúscula y minúscula
Descripción: Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 23/10/22
"""

string = input('Introduce una cadena: ')
new_string = ""
pos = 0

for i in range(pos, len(string)):
    new_string = string.swapcase()

print(new_string)
