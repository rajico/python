"""
Nombre del programa: ¿Cadena mayúscula?
Enunciado: Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente.
Pueden ocurrir tres cosas:

    El exponente sea positivo, solo tienes que imprimir la potencia.
    El exponente sea 0, el resultado es 1.
    El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

base = int(input('Introduce la base: '))
exp = int(input('Introduce el exponente: '))

if exp > 0:
    print(f'La potencia es {base}^{exp}.')
elif exp == 0:
    print(f'La potencia es 1.')
else:
    print(f'La potencia es 1/({base}^{abs(exp)}).')
