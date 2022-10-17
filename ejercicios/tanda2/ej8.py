"""
Nombre del programa: Aceptada o no aceptada.
Enunciado: Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre
el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y
el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’.
Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

# Pedimos al usuario la nota, la edad y el carácter sexo

mark = int(input('Introduce la nota: '))
age = int(input('Introduce la edad: '))
sex = input('Introduce un carácter, M o F: ')

# Creamos la estructura alternativa con if else

if mark >= 5:
    if age >= 18:
        if sex.upper() == 'F':
            print('ACEPTADA')
        if sex.upper() == 'M':
            print('POSIBLE')
else:
    print('NO ACEPTADA')
