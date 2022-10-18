"""
Nombre del programa: El mayor entre 5 números
Enunciado: Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
proporcione la calificación cualitativa correspondiente al número dado.
La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5),
«Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9),
«Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

mark = int(input('Introduce la calificación numérica del examen: '))  # Indicamos al usuario introducir la nota

if mark < 5:  # Si la nota es menor que 5...
    print('Suspenso.')  # Indicamos que está suspenso
elif 5 <= mark < 7:  # Si la nota es mayor o igual que 5, pero menor que 7...
    print('Aprobado.')  # Indicamos que está aprobado
elif 7 <= mark < 9:  # Si la nota es mayor o igual que 7, pero menor que 9...
    print('Notable.')  # Indicamos que tiene un notable
elif 9 <= mark < 10:  # Si la nota es mayor o igual que 9, pero menor que 10...
    print('Sobresaliente.')  # Indicamos que tiene un sobresaliente
elif mark == 10:  # Si la nota es igual a 10...
    print('Matrícula de honor.')  # Indicamos que tiene matrícula de honor
