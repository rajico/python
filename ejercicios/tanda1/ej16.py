# Descripción: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d.
# El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia
# entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar
# en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
# Autor del ejercicio: Rafael Jiménez Cobos

import sys

vel1 = int(input('Introduce la velocidad del primer vehículo en km/h: '))
vel2 = int(input('Introduce la velocidad del segundo vehículo en km/h: '))

if vel1 <= vel2:
    print('\nERROR. El primer vehículo no podrá alcanzar al segundo.', file=sys.stderr)
    sys.exit(1)
else:
    dist = int(input('Introduce la distancia entre los dos vehículos en km: '))

    time = 60 * dist / (vel1 - vel2)

    print('\nEl segundo vehículo alcanzará al primero en', time, 'minutos.')
