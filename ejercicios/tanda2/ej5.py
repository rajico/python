"""
Nombre del programa: ¿Quién es más joven de los dos?
Enunciado: Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

age1 = int(input('Introduce la edad de la primera persona: '))
age2 = int(input('Introduce la edad de la segunda persona: '))

if age1 > age2:
    print('La primera persona es mayor que la segunda.')
elif age1 < age2:
    print('La segunda persona es mayor que la primera.')
elif age1 == age2:
    print('Ambas personas tienen la misma edad.')
