# Descripción: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
# Autor del ejercicio: Rafael Jiménez Cobos

name = input('Escribe un nombre: ')
sur1 = input('Escribe el primer apellido: ')
sur2 = input('Escribe el segundo apellido: ')

substring1 = name[0].upper()+'.'
substring2 = sur1[0].upper()+'.'
substring3 = sur2[0].upper()+'.'

print('Las iniciales son '+substring1+substring2+substring3)
