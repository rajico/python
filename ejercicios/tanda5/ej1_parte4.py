"""
Nombre del programa: Menú de cálculos
Descripción:
Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas,
pide una opción (por su número) y devuelve la opción escogida.
Modifica el último programa para que use esta función.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/11/22
"""

opciones = ['1) Introducir A y B.', '2) Sumar.', '3) Restar.', '4) Multiplicar.', '5) Dividir.', '6) Finalizar.']


def menu(lista):
    for opt in lista:
        print(f"{opt}")

    option_input = int(input('Introduce el número de la opción correspondiente: '))

    return option_input


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

check_a_y_b = False

while True:
    print('\n---Menú---')
    option = menu(opciones)

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
    input('Pulsa Intro para continuar...')
