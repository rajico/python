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

PUNCTUATION_MARKS = ".,;:-_()\'\"?¿¡![]{}"

user_input = input('Introduce un carácter cualquiera: ')

if len(user_input) == 1:
    if PUNCTUATION_MARKS in user_input:
        print('Es signo de puntuación.')
    elif user_input.isalpha():
        print('Es una letra.')
    elif user_input.isdigit():
        print('Es un dígito.')
    else:
        print('Es otro carácter.')
else:
    print('Debes introducir un carácter.')
