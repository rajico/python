# Descripción: Dadas dos variables numéricas A y B, que el usuario debe teclear,
# se pide realizar un algoritmo que intercambie los valores de ambas variables y
# muestre cuanto valen al final las dos variables.
# Autor del ejercicio: Rafael Jiménez Cobos

a = int(input('Introduce el número A: '))
b = int(input('Introduce el número B: '))
c = 0

print('El valor original de A es:', a)
print('El valor original de B es:', b)
print('La variable auxiliar tiene un valor de', c)

c = a
a = b
b = c

print('El nuevo valor de A es:', a)
print('El nuevo valor de B es:', b)
