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

mark = int(input('Introduce la calificación numérica del examen: '))

if mark < 5:
    print('Suspenso.')
elif 5 <= mark < 7:
    print('Aprobado.')
elif 7 <= mark < 9:
    print('Notable.')
elif 9 <= mark < 10:
    print('Sobresaliente.')
elif mark == 10:
    print('Matrícula de honor.')
