"""
Nombre del programa: Aceptada o no aceptada.
Enunciado: Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre
el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y
el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’.
Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

mark = int(input('Introduce la nota: '))  # Pedimos al usuario introducir la nota
age = int(input('Introduce la edad: '))  # Pedimos al usuario introducir la edad
sex = input('Introduce un carácter, M o F: ')  # Pedimos al usuario introducir el sexo

if mark >= 5:  # Si la nota es mayor o igual a 5...
    if age >= 18:  # Y además la edad es mayor o igual a 18...
        if sex.upper() == 'F':  # Si el sexo es mujer, 'F'...
            print('ACEPTADA')  # Indicamos por pantalla ACEPTADA
        if sex.upper() == 'M':  # Si el sexo es hombre, 'M'...
            print('POSIBLE')  # Indicamos por pantalla POSIBLE
else:  # De lo contrario...
    print('NO ACEPTADA')  # Indicamos por pantalla NO ACEPTADA
