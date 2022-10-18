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

base = int(input('Introduce la base: '))  # Pedimos al usuario que introduzca la base
exp = int(input('Introduce el exponente: '))  # Pedimos al usuario que introduzca el exponente

if exp > 0:  # Si el exponente es mayor que 0...
    print(f'La potencia es {base}^{exp}.')  # Imprimimos la potencia
elif exp == 0:  # Si el exponente es exactamente igual a 0...
    print(f'La potencia es 1.')  # El resultado es 1
else:  # De lo contrario...
    print(f'La potencia es 1/({base}^{abs(exp)}).')  # El resultado es 1/potencia con el exponente positivo
