"""
Nombre del programa: Clase Duration
Descripción:
En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan,
vamos a hacer una nueva que se llamará Duration. Debe permitir:

    Crear duraciones de tiempos.
        Ejemplo: t = Time(10,20,56)
        Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    Las duraciones de tiempo se pueden comparar.
    A las duraciones de tiempo les puedo sumar y restar segundos.
    Las duraciones de tiempo se pueden sumar y restar.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 1/12/22
"""


class Duration:
    """Esta clase permite manipular las duraciones de tiempo (horas:minutos:segundos)."""
    def __init__(self, horas, minutos, segundos):
        self.segundos = 0
        self.minutos = 0
        while True:
            if segundos > 60:
                minutos += 1
                segundos -= 60
            else:
                self.segundos = segundos
                break

        while True:
            if minutos > 60:
                horas += 1
                minutos -= 60
            else:
                self.minutos = minutos
                break

        self.horas = horas

    def __eq__(self, other):
        return self.horas == other.horas and self.minutos == other.minutos and self.segundos == other.segundos

    def __str__(self):
        return f"{self.horas},{self.minutos},{self.segundos}"

    def __sumar_segundos(self, segundos):
        while True:
            if segundos > 60:
                self.minutos += 1
                segundos -= 60
            else:
                self.segundos = segundos
                break
        while True:
            if self.minutos > 60:
                self.horas += 1
                self.minutos -= 60
            else:
                break

    def __restar_segundos(self, segundos):
        seg = Duration.__segundos_total(self) - segundos
        assert seg >= 0
        result = Duration.__segundos_a_tiempo(seg)
        return result.horas, result.minutos, result.segundos

    def __sumar_duracion(self, duracion):
        seg = Duration.__segundos_total(self) + Duration.__segundos_total(duracion)
        assert seg >= 0
        result = Duration.__segundos_a_tiempo(seg)
        return result.horas, result.minutos, result.segundos

    def __restar_duracion(self, duracion):
        seg = Duration.__segundos_total(self) - Duration.__segundos_total(duracion)
        assert seg >= 0
        result = Duration.__segundos_a_tiempo(seg)
        return result.horas, result.minutos, result.segundos

    def __sub__(self, other):
        if isinstance(other, Duration):
            return Duration.__restar_duracion(self, other)
        else:
            seg = Duration.__segundos_total(self) - other
            assert seg >= 0
            result = Duration.__segundos_a_tiempo(seg)
            return result.horas, result.minutos, result.segundos

    def __add__(self, other):
        if isinstance(other, Duration):
            return Duration.__sumar_duracion(self, other)
        else:
            seg = Duration.__segundos_total(self) + other
            assert seg >= 0
            result = Duration.__segundos_a_tiempo(seg)
            return result.horas, result.minutos, result.segundos

    @classmethod
    def __segundos_total(cls, tiempo):
        return tiempo.horas * 3600 + tiempo.minutos * 60 + tiempo.segundos

    @classmethod
    def __segundos_a_tiempo(cls, s):
        horas = s // 3600
        s = s % 3600
        minutos = s // 60
        segundos = s % 60
        return Duration(horas, minutos, segundos)


if __name__ == '__main__':
    # t = Duration(10, 62, 15)
    t = Duration(10, 10, 10)
    # t1 = Duration(11, 20, 30)
    t1 = Duration(11, 11, 11)
    t2 = Duration(11, 20, 30)
    print(str(t.horas)+","+str(t.minutos)+","+str(t.segundos))

    print(f"Comparando t y t1: "+str(t == t1))
    print(f"Comparando t1 y t2: "+str(t1 == t2))

    # t2.sumar_segundos(360)

    print(f"Sumando segundos: "+str(t2))
    print(f"Sumando segundos: "+str(t2+360))
    # print(f"Restando segundos: "+str(t.restar_segundos(660)))
    print(f"Restando segundos: "+str(t - 660))

    # print(f"Sumando duraciones de tiempo:"+str(t.sumar_duracion(t1)))
    print(f"Sumando duraciones de tiempo:" + str(t1 + t))
    # print(f"Restando duraciones de tiempo:" + str(t1.restar_duracion(t)))
    print(f"Restando duraciones de tiempo:" + str(t1 - t))
