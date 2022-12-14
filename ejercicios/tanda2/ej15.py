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

student_count = int(input('¿Cuántos alumnos van a ir al viaje de estudios? '))
price = 0

if student_count >= 100:
    price = student_count * 65
elif 50 <= student_count <= 99:
    price = student_count * 70
elif 30 <= student_count <= 49:
    price = student_count * 95
else:
    price = 4000

print(f'El precio final del pago a la compañía de autobuses teniendo en cuenta '
      f'que van {student_count} alumnos, es de {price} €.')
