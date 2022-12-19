"""
Nombre del programa: Números primos
Descripción: Mostrar en pantalla los N primero número primos.
Se pide por teclado la cantidad de números primos que queremos mostrar.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 22/10/22
"""

num = int(input('Introduce la cantidad de números primos a mostrar: '))

print(f'Números primos entre 0 y {num}')

for i in range(0, num + 1):
    if i > 1:
        for x in range(2, i):
            if (i % x) == 0:
                break
        else:
            print(i)
