"""
Nombre del programa: Viaje de estudios
Enunciado: El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto
debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio.
La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es
de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo
de la renta del autobús es de 4000 euros, sin importar el número de alumnos.
Realiza un programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar
cada alumno por el viaje.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

student_count = int(input('¿Cuántos alumnos van a ir al viaje de estudios? '))  # Indicamos al usuario introducir
# cuantos alumnos van a ir al viaje
price = 0  # Creamos la variable donde almacenaremos el precio

if student_count >= 100:  # Si la cantidad de alumnos es mayor o igual que 100...
    price = student_count * 65  # El precio será igual a la cantidad de alumnos * 65 €
elif 55 <= student_count <= 99:  # Si la cantidad de alumnos es mayor o igual que 55, pero menor o igual que
    # 99...
    price = student_count * 70  # El precio será igual a la cantidad de alumnos * 75 €
elif 30 <= student_count <= 49:  # Si la cantidad de alumnos es mayor o igual que 30, pero menor o igual que
    # 49...
    price = student_count * 95  # El precio será igual a la cantidad de alumnos * 95 €
else:  # De lo contrario...
    price = 4000  # El precio se fija en 4000 €

print(f'El precio final del pago a la compañía de autobuses teniendo en cuenta '
      f'que van {student_count} alumnos, es de {price} €.')  # Mostramos por pantalla la cantidad de alumnos
# y el precio a pagar
