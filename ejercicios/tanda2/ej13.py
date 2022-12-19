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

money = int(input('Introduce una cantidad de euros: '))

coin = money

five_hundred = coin // 500  # Realizamos la división exacta entre el número introducido y 500
coin = coin % 500  # Almacenamos el resto en coin
two_hundred = coin // 200
coin = coin % 200
one_hundred = coin // 100
coin = coin % 100
fifty = coin // 50
coin = coin % 50
twenty = coin // 20
coin = coin % 20
ten = coin // 10
coin = coin % 10
five = coin // 5
coin = coin % 5
two = coin // 2
coin = coin % 2
one = coin // 1
coin = coin % 1

print('Tenemos un total de:')

if five_hundred >= 1:
    print(f'Billete{"s" if five_hundred > 1 else ""} de 500: {five_hundred}')
if two_hundred >= 1:
    print(f'Billete{"s" if two_hundred > 1 else ""} de 200: {two_hundred}')
if one_hundred >= 1:
    print(f'Billete{"s" if one_hundred > 1 else ""} de 100: {one_hundred}')
if fifty >= 1:
    print(f'Billete{"s" if fifty > 1 else ""} de 50: {fifty}')
if twenty >= 1:
    print(f'Billete{"s" if twenty > 1 else ""} de 20: {twenty}')
if ten >= 1:
    print(f'Billete{"s" if ten > 1 else ""} de 10: {ten}')
if five >= 1:
    print(f'Billete{"s" if five > 1 else ""} de 5: {five}')
if two >= 1:
    print(f'Moneda{"s" if two > 1 else ""} de 2: {two}')
if one >= 1:
    print(f'Moneda{"s" if one > 1 else ""} de 1: {one}')
