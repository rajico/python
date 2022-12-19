"""
Nombre del programa: Menú de cálculos
Descripción:
Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
Las variables se inicializan a cero.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/11/22
"""


def introducir_a_y_b():
    global a
    global b
    a = int(input('Introduce el valor de a: '))
    b = int(input('Introduce el valor de b: '))


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


a = 0
b = 0

print('\n---Menú---')
print('1) Introducir a y b.')
print('2) Sumar.')
print('3) Restar.')
print('4) Multiplicar.')
print('5) Dividir.')
print('6) Finalizar.\n')

option = int(input('Introduce el número de la función a usar: '))

if option == 1:
    introducir_a_y_b()
elif option == 2:
    sumar(a, b)
elif option == 3:
    restar(a, b)
elif option == 4:
    multiplicar(a, b)
elif option == 5:
    dividir(a, b)
elif option == 6:
    finalizar()
else:
    print(f'\n{option} no es un número de opción válido.')
