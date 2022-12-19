"""
Nombre del programa: Fibonacci Recursivo
Descripción: Cálculo el término "n" de la serie de Fibonacci de forma recursiva.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 3/11/22
"""


def fibonacci(n):
    """
    Cálculo el término "n" de la serie de Fibonacci de forma recursiva.
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """
    Función principal del programa.
    """
    num = int(input('Introduce el término de la serie de Fibonacci a calcular: '))
    print(f'El término {num} de la serie de Fibonacci es {fibonacci(num)}')


if __name__ == "__main__":
    main()
