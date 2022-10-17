# Descripción: Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
# Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
# Autor del ejercicio: Rafael Jiménez Cobos
import math

num = int(input('Introduce un número: '))
sq_num = math.sqrt(num)
cb_num = math.pow(num, 1.0/3.0)

print('La raíz cuadrada de', num, 'es:', sq_num)
print('La raíz cúbica de', num, 'es: '+repr(cb_num))
