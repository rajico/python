"""
Nombre del programa: Conversor de palotes
Descripción: Crea una función que reciba un número, lo convierta al sistema de palotes
y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 19/11/22
"""

NUM = int(input('Introduce un número: '))


def convertir_en_palotes(num):
    """
    Función convertir_en_palotes
    Descripción: Esta función convierte el número dado como parámetro al sistema de palotes.
    Forma de uso: convertir_en_palotes(num)
    :param num:
    :return:
    """
    cad = str(num)
    palote = ''

    for i in range(0, len(cad)):
        if int(cad[i]) == 0:
            palote = palote + "-" * 1
        if int(cad[i]) != 0:
            palote = palote + "|" * int(cad[i])
        if i < len(cad) - 1 and int(cad[i]) != 0:
            palote = palote + "-"

    return palote


def main():
    print(convertir_en_palotes(NUM))


if __name__ == '__main__':
    main()
