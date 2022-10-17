# Descripción: Calcular la media de tres números pedidos por teclado.
# Autor del ejercicio: Rafael Jiménez Cobos

from statistics import mean

num1 = int(input('Inserta el primer número: '))
num2 = int(input('Inserta el segundo número: '))
num3 = int(input('Inserta el tercer número: '))

avg = mean([num1, num2, num3])

print('La media de los números', num1, num2, 'y', num3, 'es:', avg)
