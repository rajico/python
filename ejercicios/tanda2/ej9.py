"""
Nombre del programa: Identificador de caracteres
Enunciado: Diseña un programa que lea un carácter de teclado y muestre por pantalla el
mensaje «Es signo de puntuación» solo si el carácter leído es un signo de puntuación,
«Es una letra» si es una letra (da igual que sea mayúscula, minúscula o acentuada),
«Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores
y «No es un carácter» si el usuario ha introducido más de un carácter.

Pista: quizás te pueda venir bien usar el método find de la clase str.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

import re  # Importamos la librería 're' para trabajar con expresiones regulares

user_input = input('Introduce un carácter cualquiera: ')  # Pedimos al usuario que introduzca cualquier carácter

if len(user_input) == 1:  # Si la longitud de la cadena introducida es exactamente igual a 1...
    if re.search("[.,;:-_()\'\"?¿¡!]", user_input):  # Si encontramos un carácter de puntuación...
        print('Es signo de puntuación.')  # Lo indicamos por pantalla
    elif re.search("[a-zA-Z]", user_input) or re.search("[áéíóúÁÉÍÓÚ]", user_input):  # Si encontramos una letra...
        print('Es una letra.')  # Lo indicamos por pantalla
    elif re.search("[0-9]", user_input):  # Si encontramos un número...
        print('Es un dígito.')  # Lo indicamos por pantalla
    else:  # De lo contrario...
        print('Es otro carácter.')  # Indicamos que se trata de otro carácter no planteado en el programa
else:  # De lo contrario...
    print('No es un carácter.')  # Indicamos por pantalla que no se trata de un solo carácter
