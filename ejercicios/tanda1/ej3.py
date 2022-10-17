# Descripción: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
# Autor del ejercicio: Rafael Jiménez Cobos

from math import sqrt as sq

cat1 = float(input('Introduce el valor del primer cateto: '))
cat2 = float(input('Introduce el valor del segundo cateto: '))

hip = sq(cat1**2+cat2**2)

print('La hipotenusa es', hip)
