"""
Nombre del programa: Coste de la entrega de un paquete
Enunciado: Una compañía de transporte internacional tiene servicio en algunos países de América del Norte,
América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el
peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:

ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto
por cuestiones de logística y de seguridad.

Realice un algoritmo para determinar el cobro por la entrega de un paquete o,
en su caso, el rechazo de la entrega.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

print('ZONA	UBICACIÓN	COSTO/GRAMO')
print('1	América del Norte	24.00 euros')
print('2	América Central	20.00 euros')
print('3	América del Sur	21.00 euros')
print('4	Europa	10.00 euros')
print('5	Asia	18.00 euros\n')

zone = int(input('Introduce el número de la zona a la que quieres enviar el paquete: '))
weight = float(input('Introduce el peso del paquete en gramos: '))
price = 0

if weight < 5000:
    if zone == 1:
        price = weight * 24 / 1000
    elif zone == 2:
        price = weight * 20 / 1000
    elif zone == 3:
        price = weight * 21 / 1000
    elif zone == 4:
        price = weight * 10 / 1000
    elif zone == 5:
        price = weight * 18 / 1000
    else:
        print(f'{zone} no es un código de zona válido.')
    print(f'El envío de tu paquete a la zona introducida costaría {price:.2f}€.')
else:
    print('La entrega ha sido rechazada debido a que el peso del paquete supera los 5 kilos.')
