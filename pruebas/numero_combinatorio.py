"""
Nombre del programa: Cálculo de número combinatorio
Descripción: Primera prueba de funciones. Se piden dos números, n y m y se calcula cuál es el número combinatorio
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 2/11/22
"""


def factorial(x):
    f = 1
    for i in range(x, 1, -1):
        f = f*i
    return f


# Pedimos los datos: n y m de forma que n > m
while True:
    n = int(input("indique el valor de n (recuerde que debe ser mayor que m) "))
    m = int(input("indique el valor de m (recuerde que debe ser menor que n) "))
    if n > m:
        break

combinatorio = factorial(n) / (factorial(m) * factorial(n-m))

# Resultado
print(f"El número combinatorio de {n} sobre {m} es {combinatorio}")
