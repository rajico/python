"""
Nombre del programa: Clase Fraction
Descripción:
Crea una clase, y pruébala, que modele fracciones. Debe permitir:

    Crear fracciones indicando numerador y denominador.
        Ejemplo: f = Fraction(2, 3)
        Ojo!!! No se puede tener un denominador cero.
    Las fracciones pueden operar entre sí.
        Sumar, multiplicar, dividir, restar.
        Ojo!!! esto se puede hacer: f + 1, 5 * f
    Las fracciones se pueden comparar.
        ==, <, <=, >, >=, !=
        Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
        Ojo!!! esto se puede hacer 1 < 1/2
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/12/22
"""


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        assert denominator != 0

    def __add__(self, number):
        if isinstance(number, int):
            new_numerator = self.numerator + (number * self.denominator)
            new_denominator = self.denominator * 1
        elif isinstance(number, Fraction):
            new_denominator = Fraction.calcular_mcm(self, number)
            new_numerator = (self.numerator * number.denominator) + (self.denominator * number.numerator)
        else:
            raise Exception("Solo se permite sumar números enteros y fracciones.")
        return str(new_numerator) + "/" + str(new_denominator)

    def __sub__(self, number):
        if isinstance(number, int):
            new_numerator = self.numerator - (number * self.denominator)
            new_denominator = self.denominator * 1
        elif isinstance(number, Fraction):
            new_denominator = Fraction.calcular_mcm(self, number)
            new_numerator = (self.numerator * number.denominator) - (self.denominator * number.numerator)
        else:
            raise Exception("Solo se permite restar números enteros y fracciones.")
        return str(new_numerator) + "/" + str(new_denominator)

    def __mul__(self, number):
        if isinstance(number, int):
            new_numerator = number * self.numerator
            new_denominator = 1 * self.denominator
        elif isinstance(number, Fraction):
            new_numerator = self.numerator * number.numerator
            new_denominator = self.denominator * number.denominator
        else:
            raise Exception("Solo se permite multiplicar números enteros y fracciones.")
        return str(new_numerator) + "/" + str(new_denominator)

    def __truediv__(self, number):
        if isinstance(number, int):
            new_numerator = 1 * self.numerator
            new_denominator = number * self.denominator
        elif isinstance(number, Fraction):
            new_numerator = self.numerator * number.denominator
            new_denominator = self.denominator * number.numerator
        else:
            raise Exception("Solo se permite dividir números enteros y fracciones.")
        return str(new_numerator) + "/" + str(new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return self.numerator != other.numerator and self.denominator != other.denominator

    def __lt__(self, other):
        return self.numerator < other.numerator and self.denominator < other.numerator

    def __le__(self, other):
        return self.numerator < other.numerator and self.denominator < other.numerator or \
            self.numerator == other.numerator and self.denominator == other.denominator

    def __gt__(self, other):
        return self.numerator > other.numerator and self.denominator > other.numerator

    def __ge__(self, other):
        return self.numerator > other.numerator and self.denominator > other.numerator or \
            self.numerator == other.numerator and self.denominator == other.denominator

    @staticmethod
    def calcular_mcd(f1, f2):
        temporal = 0
        a = f1.denominator
        b = f2.denominator
        while b != 0:
            temporal = b
            b = a % b
            a = temporal
        return a

    @staticmethod
    def calcular_mcm(f1, f2):
        a = f1.denominator
        b = f2.denominator
        return (a * b) / Fraction.calcular_mcd(f1, f2)


if __name__ == '__main__':
    f = Fraction(5, 2)
    f_1 = Fraction(2, 5)
    f_2 = Fraction(2, 5)
    f_3 = Fraction(1, 1)
    print(str(f.numerator) + "/" + str(f.denominator))

    print("Suma de número entero + fracción: ", str(f + 1))
    print("Suma de fracciones: ", str(f + f_1))
    print("Resta de número entero - fracción: ", str(f - 1))
    print("Resta de fracciones: ", str(f - f_1))

    print("Multiplicación de número entero * fracción: ", str(f * 2))
    print("Multiplicación de fracciones: ", str(f * f_1))
    print("División de número entero / fracción: ", str(f / 2))
    print("División entre fracciones: ", str(f / f_1))

    print("Comprobación: ¿Son iguales estas fracciones?", str(f_1 == f_2))
    print("Comprobación: ¿Son iguales estas fracciones?", str(f == f_1))

    print("Comprobación: ¿Son diferentes estas fracciones?", str(f_1 != f_2))
    print("Comprobación: ¿Son diferentes estas fracciones?", str(f != f_3))

    print("Comprobación: ¿Es menor la primera fracción que la segunda?", str(f_1 < f_3))
    print("Comprobación: ¿Es menor la primera fracción que la segunda?", str(f_3 < f_1))

    print("Comprobación: ¿Es menor o igual la primera fracción que la segunda?", str(f_1 <= f_3))
    print("Comprobación: ¿Es menor o igual la primera fracción que la segunda?", str(f_1 <= f_2))

    print("Comprobación: ¿Es mayor la primera fracción que la segunda?", str(f_1 > f_3))
    print("Comprobación: ¿Es mayor la primera fracción que la segunda?", str(f_3 > f_1))

    print("Comprobación: ¿Es mayor o igual la primera fracción que la segunda?", str(f_1 >= f_3))
    print("Comprobación: ¿Es mayor o igual la primera fracción que la segunda?", str(f_3 >= f_1))
