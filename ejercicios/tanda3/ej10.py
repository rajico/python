"""
Nombre del programa: Contar en cadena
Descripción: Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 22/10/22
"""

get_string = input('Introduce una cadena: ')
get_char = input('Introduce el carácter a buscar: ')
counter = 0

for i in get_string:
    counter = get_string.count(get_char)

print(f'El carácter {get_char} se ha encontrado un total de {counter} veces')
