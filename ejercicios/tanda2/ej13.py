"""
Nombre del programa: Contador de euros
Enunciado: Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 y 1 €.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente resultado:

    2 billetes de 200 euros.
    1 billete de 20 euros.
    1 billete de 10 euros.
    2 monedas de 2 euros.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Pedimos al usuario introducir una cantidad de euros

money = int(input('Introduce una cantidad de euros: '))

# Contamos cada euro

euro = money

five_hundred = euro // 500
aux1 = euro % 500
two_hundred = aux1 // 200
aux2 = aux1 % 200
one_hundred = aux2 // 100
aux3 = aux2 % 100
fifty = aux3 // 50
aux4 = aux3 % 50
twenty = aux4 // 20
aux5 = aux4 % 20
ten = aux5 // 10
aux6 = aux5 % 10
five = aux6 // 5
aux7 = aux6 % 5
two = aux7 // 2
aux8 = aux7 % 2
one = aux8 // 1
aux9 = aux8 % 1

print('Tenemos un total de:')

if five_hundred >= 1:
    print(f'Billetes de 500: {five_hundred}')
if two_hundred >= 1:
    print(f'Billetes de 200: {two_hundred}')
if one_hundred >= 1:
    print(f'Billetes de 100: {one_hundred}')
if fifty >= 1:
    print(f'Billetes de 50: {fifty}')
if twenty >= 1:
    print(f'Billetes de 20: {twenty}')
if ten >= 1:
    print(f'Billetes de 10: {ten}')
if five >= 1:
    print(f'Billetes de 5: {five}')
if two >= 1:
    print(f'Monedas de 2: {two}')
if one >= 1:
    print(f'Monedas de 1: {one}')
