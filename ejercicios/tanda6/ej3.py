"""
Nombre del programa: Clase Date
Descripción:
En Python podemos manejar pero no nos gusta, vamos a crear una clase Date. Debe permitir:

    Crear fechas.
        Ejemplo: f = Date(17, 11, 2022)
        Ojo!!! Estas fechas son erróneas:
            Date(78, -45, 0)
            Date(31, 6, 2022)
            Date(29, 2, 2022)
    Las fechas se pueden comparar.
    A las fechas se le pueden sumar y restar días.
    Las fechas se pueden restar. (sobrecarga de operadores con -)
    Se debe poder averiguar el día de la semana de una fecha.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/12/22
"""


class Date:
    MESES_CON_30D = [4, 6, 9, 11]
    MESES_CON_31D = [1, 3, 5, 7, 8, 10, 12]

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if not Date.validar_fecha(self):
            raise Exception("La fecha no es correcta, introduce otra.")

    def __eq__(self, fecha):
        return self.day == fecha.day and self.month == fecha.month and self.year == fecha.year

    def __ne__(self, fecha):
        return self.day != fecha.day and self.month != fecha.month and self.year != fecha.year

    def __gt__(self, fecha):
        return self.day > fecha.day and self.month > fecha.month and self.year > fecha.year

    def __ge__(self, fecha):
        return self.day > fecha.day and self.month > fecha.month and self.year > fecha.year or \
            self.day == fecha.day and self.month == fecha.month and self.year == fecha.year

    def __lt__(self, fecha):
        return self.day < fecha.day and self.month < fecha.month and self.year < fecha.year

    def __le__(self, fecha):
        return self.day < fecha.day and self.month < fecha.month and self.year < fecha.year or \
            self.day == fecha.day and self.month == fecha.month and self.year == fecha.year

    def __str__(self):
        return f"{self.day},{self.month},{self.year}"

    def __sumar_dia(self):
        dia = self.day + 1
        mes = self.month
        anyo = self.year
        if (mes in Date.MESES_CON_30D and dia > 30) or (mes in Date.MESES_CON_31D and dia > 31) \
                or ((Date.__es_bisiesto(self) and dia > 29) or (not Date.__es_bisiesto(self) and dia > 28)):
            # mes siguiente
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                anyo += 1

        self.day = dia
        self.month = mes
        self.year = anyo

    def __restar_dia(self):
        dia = self.day - 1
        mes = self.month
        anyo = self.year
        if mes in Date.MESES_CON_30D and dia < 1:
            dia = 30
            mes -= 1
        elif mes in Date.MESES_CON_31D and dia < 1:
            dia = 31
            mes -= 1
        elif Date.__es_bisiesto(self) and dia < 1:
            dia = 29
            mes -= 1
        elif not Date.__es_bisiesto(self) and dia < 1:
            dia = 28
            mes -= 1
        if mes < 1:  # nos pasamos de diciembre, año siguiente
            mes = 12
            anyo -= 1

        self.day = dia
        self.month = mes
        self.year = anyo

    def sumar_x_dias(self, dias):
        for i in range(dias):
            self.__sumar_dia()

    def restar_x_dias(self, dias):
        for i in range(dias):
            self.__restar_dia()

    def __sub__(self, fecha):
        if self.day == fecha.day:
            dia = self.day
        else:
            if self.day > fecha.day:
                dia = self.day - fecha.day
            else:
                print("Como el día de la segunda fecha es mayor, se va a intercambiar por el día de la primera fecha.")
                dia = fecha.day - self.day

        if self.month == fecha.month:
            mes = self.month
        else:
            if self.month > fecha.month:
                mes = self.month - fecha.month
            else:
                print("Como el mes de la segunda fecha es mayor, se va a intercambiar por el mes de la primera fecha.")
                mes = fecha.month - self.month

        if self.year == fecha.year:
            anyo = self.year
        else:
            if self.year > fecha.year:
                anyo = self.year - abs(self.year - fecha.year)
            else:
                print("Como el año de la segunda fecha es mayor, se va a intercambiar por el año de la primera fecha.")
                anyo = fecha.year - abs(fecha.year - self.year)

        if mes in Date.MESES_CON_30D and dia < 1:
            dia = 30
            mes -= 1
        elif mes in Date.MESES_CON_31D and dia < 1:
            dia = 31
            mes -= 1
        elif Date.__es_bisiesto(self) and dia < 1:
            dia = 29
            mes -= 1
        elif not Date.__es_bisiesto(self) and dia < 1:
            dia = 28
            mes -= 1
        if mes < 1:  # nos pasamos de diciembre, año siguiente
            mes = 12
            anyo -= 1

        return dia, mes, anyo

    def dia_de_la_semana(self):
        a = int((14 - self.month) / 12)
        y = self.year - a
        m = int(self.month + (12 * a) - 2)
        d = int(self.day + y + int(y / 4) - int(y / 100) + int(y / 400) + ((31 * m) / 12)) % 7

        if d == 0:
            dia_semana = 'Domingo'
        elif d == 1:
            dia_semana = 'Lunes'
        elif d == 2:
            dia_semana = 'Martes'
        elif d == 3:
            dia_semana = 'Miércoles'
        elif d == 4:
            dia_semana = 'Jueves'
        elif d == 5:
            dia_semana = 'Viernes'
        else:
            dia_semana = 'Sábado'
        return dia_semana

    @classmethod
    def validar_fecha(cls, fecha):
        day = fecha.day
        month = fecha.month
        year = fecha.year
        if 0 > len(str(fecha.day)) > 2:
            raise Exception("La cifra del día no puede ser inferior a 0 o superior a 2.")
        if fecha.day == 0 or fecha.day < 0:
            raise Exception("El día no puede ser 0 o inferior.")
        if 0 > len(str(fecha.month)) > 2:
            raise Exception("La cifra del mes no puede ser inferior a 0 o superior a 2.")
        if fecha.month == 0 or fecha.month < 0:
            raise Exception("El mes no puede ser 0 o inferior.")
        if 0 > len(str(fecha.year)) > 4:
            raise Exception("La cifra del año no puede ser inferior a 0 o superior a 4.")
        if fecha.year == 0 or fecha.year < 0:
            raise Exception("El año no puede ser 0 o inferior.")
        check = False

        if month in Date.MESES_CON_30D and 30 >= day > 0:
            check = True
        elif month in Date.MESES_CON_31D and 31 >= day > 0:
            check = True
        elif month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and 29 >= day > 0:
                check = True
            elif 28 >= day > 0:
                check = True
        if year < 0:
            check = False
        return check

    @classmethod
    def __es_bisiesto(cls, fecha):
        return fecha.year % 4 == 0 and (fecha.year % 100 != 0 or fecha.year % 400 == 0)


if __name__ == '__main__':
    f = Date(28, 2, 2022)
    f_1 = Date(28, 2, 2022)

    print(str(f == f_1))

    print(f"Sumando días a {f}: ")
    f.sumar_x_dias(2)
    print(str(f), "\n")

    f_prueba = Date(1, 1, 2023)

    print(f"Restando días a {f_prueba}: ")
    f_prueba.restar_x_dias(2)
    print(str(f_prueba))

    f_10 = Date(5, 1, 2023)
    f_11 = Date(2, 2, 2023)
    f_12 = Date(5, 1, 2023)
    f_13 = Date(3, 1, 2022)

    f_ene = Date(1, 1, 2023)
    f_dic = Date(31, 12, 2022)

    print("Restando dos fechas:", f_10 - f_11)
    print("Restando dos fechas:", f_12 - f_13)
    print("Restando dos fechas:", f_11 - f_13)

    print("Restando dos fechas:", f_ene - f_dic)

    fecha_actual = Date(8, 1, 2023)

    print("Día de la semana:", str(fecha_actual.dia_de_la_semana()))
