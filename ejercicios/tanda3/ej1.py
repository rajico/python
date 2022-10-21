"""
Nombre del programa: Adivina un número
Descripción: Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo).
El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado)
si se llega al límite de intentos te muestra el número que había generado.

Para usar números aleatorios en Python: http://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/10/22

Estructura

1) Se genera un número aleatorio entre 1 y 100
2) Se piden números y respondiendo si el número es mayor o menor al introducido, así como el número de intentos
que te quedan (10 intentos)
3) El programa finaliza cuando aciertas el número (indicando el número de intentos), si se llega al límite
de intentos, se muestra el número generado
"""

import random

TRIES = 10
START_NUM = 1
END_NUM = 11

ran_num = random.randrange(1, 100)
num_list = []

for i in range(START_NUM, END_NUM):
    guess_number = int(input('\nAdivina el número aleatorio: '))
    if guess_number not in num_list:
        num_list.append(guess_number)
        if guess_number > ran_num:
            print(f'\nEl número introducido es mayor.')
        if guess_number < ran_num:
            print(f'\nEl número introducido es menor.')
        if guess_number == ran_num:
            print(f'\n¡Enhorabuena, has acertado! Has necesitado un total de {i} intentos.')
            break
        TRIES = TRIES - 1
        print(f'\nTe quedan {TRIES} intentos, prueba de nuevo.')
        if TRIES == 0:
            print(f'\nHas agotado todos los intentos, el número era {ran_num}.')
    else:
        print(f'\nEste número ya ha sido introducido, por favor, introduce otro número.')
