"""
Nombre del programa: Menú de cálculos
Descripción:
Modifica el programa anterior para que si no se introducen las dos variables desde la opción
correspondiente no se puedan ejecutar el resto de las opciones.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/11/22
"""


def introducir_a_y_b():
    global a, b, check_a_y_b
    a = int(input('Introduce el valor de a: '))
    b = int(input('Introduce el valor de b: '))
    check_a_y_b = True


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
option = 0

check_a_y_b = False

while option != 6:
    print('\n---Menú---')
    print('1) Introducir A y B.')
    print('2) Sumar.')
    print('3) Restar.')
    print('4) Multiplicar.')
    print('5) Dividir.')
    print('6) Finalizar.\n')

    option = int(input('Introduce el número de la opción correspondiente: '))

    if option == 1:
        introducir_a_y_b()
    elif option == 6:
        finalizar()
    elif check_a_y_b:
        if option == 2:
            sumar(a, b)
        elif option == 3:
            restar(a, b)
        elif option == 4:
            multiplicar(a, b)
        elif option == 5:
            dividir(a, b)
    else:
        print(f'\n{option} no es un número de opción válido.')
