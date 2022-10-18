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

money = int(input('Introduce una cantidad de euros: '))  # Pedimos al usuario introducir una cantidad de euros

coin = money  # Creamos la variable coin, con la que controlaremos la cantidad de billetes o monedas

five_hundred = coin // 500  # Realizamos la división exacta entre el número introducido y 500
coin = coin % 500  # Almacenamos el resto en coin
two_hundred = coin // 200  # Realizamos la división exacta entre el número introducido y 200
coin = coin % 200  # Almacenamos el resto en coin
one_hundred = coin // 100  # Realizamos la división exacta entre el número introducido y 100
coin = coin % 100  # Almacenamos el resto en coin
fifty = coin // 50  # Realizamos la división exacta entre el número introducido y 50
coin = coin % 50  # Almacenamos el resto en coin
twenty = coin // 20  # Realizamos la división exacta entre el número introducido y 20
coin = coin % 20  # Almacenamos el resto en coin
ten = coin // 10  # Realizamos la división exacta entre el número introducido y 10
coin = coin % 10  # Almacenamos el resto en coin
five = coin // 5  # Realizamos la división exacta entre el número introducido y 5
coin = coin % 5  # Almacenamos el resto en coin
two = coin // 2  # Realizamos la división exacta entre el número introducido y 2
coin = coin % 2  # Almacenamos el resto en coin
one = coin // 1  # Realizamos la división exacta entre el número introducido y 1
coin = coin % 1  # Almacenamos el resto en coin

print('Tenemos un total de:')

if five_hundred >= 1:  # Si la cantidad de billetes de 500 es mayor o igual a 1...
    print(f'Billetes de 500: {five_hundred}')  # Mostramos la cantidad
if two_hundred >= 1:  # Si la cantidad de billetes de 200 es mayor o igual a 1...
    print(f'Billetes de 200: {two_hundred}')  # Mostramos la cantidad
if one_hundred >= 1:  # Si la cantidad de billetes de 100 es mayor o igual a 1...
    print(f'Billetes de 100: {one_hundred}')  # Mostramos la cantidad
if fifty >= 1:  # Si la cantidad de billetes de 50 es mayor o igual a 1...
    print(f'Billetes de 50: {fifty}')  # Mostramos la cantidad
if twenty >= 1:  # Si la cantidad de billetes de 20 es mayor o igual a 1...
    print(f'Billetes de 20: {twenty}')  # Mostramos la cantidad
if ten >= 1:  # Si la cantidad de billetes de 10 es mayor o igual a 1...
    print(f'Billetes de 10: {ten}')  # Mostramos la cantidad
if five >= 1:  # Si la cantidad de billetes de 5 es mayor o igual a 1...
    print(f'Billetes de 5: {five}')  # Mostramos la cantidad
if two >= 1:  # Si la cantidad de monedas de 2 es mayor o igual a 1...
    print(f'Monedas de 2: {two}')  # Mostramos la cantidad
if one >= 1:  # Si la cantidad de monedas de 1 es mayor o igual a 1...
    print(f'Monedas de 1: {one}')  # Mostramos la cantidad
