# Descripción: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia
# entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar
# en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
# Autor del ejercicio: Rafael Jiménez Cobos

dist = int(input('Introduce la distancia entre los dos vehículos en km: '))
vel1 = int(input('Introduce la velocidad del primer vehículo en km/h: '))
vel2 = int(input('Introduce la velocidad del segundo vehículo en km/h: '))
time = 60 * dist / (vel1 - vel2)

print('El segundo vehículo alcanzará al primero en', time, 'minutos.')
