# Descripción: Pide al usuario dos números y muestra la "distancia" entre ellos
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
# Autor del ejercicio: Rafael Jiménez Cobos

num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
dist = abs(num1 - num2)

print('La distancia entre', num1, 'y', num2, 'es', dist)
