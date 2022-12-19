"""
Nombre del programa: Menú de cálculos
Descripción:
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cuatro opciones: sumar, restar,
multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables
y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/11/22
"""


def sumar(num1, num2):
    suma = num1 + num2
    print(f'{num1} + {num2} = {suma}')


def restar(num1, num2):
    resta = num1 - num2
    print(f'{num1} - {num2} = {resta}')


def multiplicar(num1, num2):
    multiplica = num1 * num2
    print(f'{num1} * {num2} = {multiplica}')


def dividir(num1, num2):
    divide = num1 / num2
    print(f'{num1} / {num2} = {divide}')


def finalizar():
    exit()


a = int(input('Introduce el primer número: '))
b = int(input('Introduce el segundo número: '))

print('\n---Menú---')
print('1) Sumar.')
print('2) Restar.')
print('3) Multiplicar.')
print('4) Dividir.')
print('5) Finalizar.\n')

option = int(input('Introduce el número de la función a usar: '))

if option == 1:
    sumar(a, b)
elif option == 2:
    restar(a, b)
elif option == 3:
    multiplicar(a, b)
elif option == 4:
    dividir(a, b)
elif option == 5:
    finalizar()
else:
    print(f'\n{option} no es un número de opción válido.')
