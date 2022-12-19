"""
Nombre del programa: Mezclar elementos de dos arrays de forma alterna
Descripción: Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra
que es el resultado de mezclar los números de ambos de forma alterna, se coge un número de a, luego de b,
luego de a, etc. Los arrays a y b pueden tener longitudes diferentes; por tanto, si se terminan los
números de un array se terminan de coger todos los que quedan del otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 25/11/22
"""


def mezclar_arrays(arr1, arr2):
    """
    Función mezclar_arrays
    Descripción: Esta función mezcla elementos de dos array de forma alterna. Es decir, mostrará
    el primer elemento del array1, el primer elemento del array2, etc...
    Forma de uso: mezclar_arrays(arr1, arr2)
    :param arr1:
    :param arr2:
    :return:
    """
    arr3 = []

    for i in zip(arr1, arr2):
        arr3.extend(i)

    if len(arr1) != len(arr2):
        arrs = [arr1, arr2]
        min_arr = min(arrs, key=len)
        max_arr = max(arrs, key=len)
        rest = max_arr[len(min_arr):]
        arr3.extend(rest)

    return arr3


def main():
    lst1 = [0, 2, 4]
    lst2 = [1, 3]
    print(mezclar_arrays(lst1, lst2))


if __name__ == "__main__":
    main()
