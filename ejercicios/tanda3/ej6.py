"""
Nombre del programa: Resolviendo potencias
Descripción: Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente)
saque por pantalla el resultado de la potencia. No se puede utilizar el operador de potencia ni la función.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 22/10/22
"""

base = float(input('Introduce la base: '))
exp = int(input('Introduce el exponente: '))

while exp <= 0:
    print('El exponente no es positivo, introdúcelo de nuevo.')
    exp = int(input('Introduce el exponente: '))

res = base

for i in range(1, exp):
    res = res * base

print(f'El resultado es {res:.2f}.')
