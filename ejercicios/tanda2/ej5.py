"""
Nombre del programa: ¿Quién es más joven de los dos?
Enunciado: Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

age1 = int(input('Introduce la edad de la primera persona: '))  # Pedimos al usuario la edad de la primera persona
age2 = int(input('Introduce la edad de la segunda persona: '))  # Pedimos al usuario la edad de la segunda persona

if age1 > age2:  # Si la primera persona es mayor que la segunda...
    print('La primera persona es mayor que la segunda.')  # Lo indicamos
elif age1 < age2:  # Si, por lo contrario, la segunda persona es mayor...
    print('La segunda persona es mayor que la primera.')  # Lo indicamos
elif age1 == age2:  # Si ambas personas tienen la misma edad...
    print('Ambas personas tienen la misma edad.')  # Lo indicamos
