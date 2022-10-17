# Descripción: Escribir un programa que convierta un valor dado en grados
# Fahrenheit a grados Celsius.
# Autor del ejercicio: Rafael Jiménez Cobos

deg_f = int(input('Introduce los grados Fahrenheit: '))
deg_c = int((deg_f-32) * 5 / 9)

print(deg_f, 'grados Fahrenheit son', deg_c, 'grados Celsius.')
