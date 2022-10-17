# Descripción: Pide al usuario dos pares de números x1,y1 y x2,y2
# que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
# Autor del ejercicio: Rafael Jiménez Cobos

x1 = int(input('Introduce el valor x1: '))
y1 = int(input('Introduce el valor y1: '))
x2 = int(input('Introduce el valor x2: '))
y2 = int(input('Introduce el valor y2: '))

result = ((((x2 - x1)**2) + ((y2-y1)**2))**0.5)

print("La distancia entre los puntos", (x1, x2), "y los puntos", (y1, y2), "es : ", result)
