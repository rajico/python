"""
Nombre del programa: Biblioteca de funciones
Descripción:
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones.
Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado
te puedes ahorrar mucho trabajo. Por ejemplo, la función es_capicúa()
resulta trivial teniendo voltea() y la función siguiente_primo() también es muy fácil de
implementar teniendo es_primo().

Prohibido usar funciones de conversión del número a una cadena.

es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.
digitos: devuelve el número de dígitos de un número entero.
voltea: le da la vuelta a un número.
digito_n: devuelve el dígito que está en la posición n de un número entero.
Se empieza contando por el 0 y de izquierda a derecha.
posicion_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero.
Si no se encuentra, devuelve -1.
quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).
quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).
pega_por_detras: añade un dígito a un número por detrás.
pega_por_delante: añade un dígito a un número por delante.
trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número
y devuelve el trozo correspondiente.
juntaNumeros: pega dos números para formar uno.

Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 20/11/22
"""
NUMBER = int(input('Introduce un número: '))


def digitos(number):
    """
    Función digitos
    Descripción: devuelve el número de dígitos de un número entero.
    Modo de uso: digitos(number)
    :param number:
    :return:
    """
    digits = 0

    while number > 0:
        number = number // 10
        digits += 1

    return digits


def digito_n(number, number_position):
    """
    Función digito_n
    Descripción: devuelve el dígito que está en la posición n de un número entero.
    Se empieza contando por el 0 y de izquierda a derecha.
    Modo de uso: digito_n(number, number_position)
    :param number:
    :param number_position:
    :return:
    """
    if number_position > digitos(number) - 1:
        return ValueError(f"¡ERROR! La máxima posición es {digitos(number) - 1}. Introduce una posición menor. \n")
    else:
        number_position = digitos(number) - 1 - number_position

        number = number // 10 ** number_position
        number = number % 10

        return number


def posicion_de_digito(number1, number2):
    """
    Función posicion_de_digito
    Descripción: da la posición de la primera ocurrencia de un dígito dentro de un número entero.
    Si no se encuentra, devuelve -1.
    Forma de uso: posicion_de_digito(number1, number2)
    :param number1:
    :param number2:
    :return:
    """

    for num_position in range(digitos(number1)):
        if number2 == digito_n(number1, num_position):
            return num_position

    return -1


def pega_por_detras(number1, number2):
    """
    Función pega_por_detras
    Descripción: añade un dígito a un número por detrás.
    Forma de uso: pega_por_detras(number1, number2)
    :param number1:
    :param number2:
    :return:
    """
    return number1 * 10 + number2


def pega_por_delante(number1, number2):
    """
    Función pega_por_delante
    Descripción: añade un dígito a un número por delante.
    Forma de uso: pega_por_delante(number1, number2)
    :param number1:
    :param number2:
    :return:
    """
    return number1 + number2 * 10 ** digitos(number1)


def junta_numeros(number1, number2):
    """
    Función junta_numeros
    Descripción: pega dos números para formar uno.
    Forma de uso: junta_numeros(number1, number2)
    :param number1:
    :param number2:
    :return:
    """
    return number1 * 10 ** digitos(number1) + number2


def voltea(number):
    """
    Función voltea
    Descripción: le da la vuelta a un número.
    Forma de uso: voltea(number)
    :param number:
    :return:
    """
    digits, num_aux = digitos(number) - 1, 0

    while number > 0:
        if digits == 0:
            num_aux += number % 10
        else:
            num_aux += (number % 10) * 10 ** digits
        number = number // 10
        digits -= 1

    return num_aux


def es_capicua(number):
    """
    Función es_capicua
    Descripción: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
    Forma de uso: es_capicua(number)
    :param number:
    :return:
    """
    if number == voltea(number):
        return True
    else:
        return False


def es_primo(number):
    """
    Función es_primo
    Descripción: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
    Forma de uso: es_primo(number)
    :param number:
    :return:
    """
    for i in range(2, int(number ** 0.5 + 1)):
        if (number % 1) == 0:
            return False

    return True


def siguiente_primo(number):
    """
    Función siguiente_primo
    Descripción: devuelve el menor primo que es mayor al número que se pasa como parámetro.
    Forma de uso: siguiente_primo(number)
    :param number:
    :return:
    """
    number = number + 1
    while True:
        if es_primo(number):
            return number
        else:
            number += 1


def main():
    """
    Función main
    Descripción: Función principal con la que se ejecutarán el resto de funciones.
    Forma de uso: main()
    :return:
    """
    print(f"Se van a ejecutar siguientes funciones usando el número {NUMBER}:")
    print(digitos(NUMBER))
    print(digito_n(NUMBER, 2))
    print(posicion_de_digito(4, NUMBER))
    print(pega_por_detras(NUMBER, 5))
    print(pega_por_delante(NUMBER, 5))
    print(junta_numeros(NUMBER, 4))
    print(voltea(NUMBER))
    print(es_capicua(343))
    print(es_capicua(NUMBER))
    print(es_primo(3))
    print(es_primo(NUMBER))
    print(siguiente_primo(1))


if __name__ == '__main__':
    main()
