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

zone = int(input('Introduce el número de la zona a la que quieres enviar el paquete: '))  # Indicamos al usuario
# introducir el número correspondiente a la zona donde quiere enviar el paquete
weight = float(input('Introduce el peso del paquete en gramos: '))  # Indicamos al usuario introducir el peso
# del paquete en gramos
price = 0  # Creamos la variable donde almacenaremos el precio final

if weight < 5000:  # Si el peso es inferior a 5kg...
    if zone == 1:  # Si es la primera zona...
        price = weight * 24 / 1000  # El precio será igual al peso * 24 (pasado a kg)
    elif zone == 2:  # Si es la segunda zona...
        price = weight * 20 / 1000  # El precio será igual al peso * 20
    elif zone == 3:  # Si es la tercera zona...
        price = weight * 21 / 1000  # El precio será igual al peso * 21
    elif zone == 4:  # Si es la cuarta zona...
        price = weight * 10 / 1000  # El precio será igual al peso * 10
    elif zone == 5:  # Si es la quinta zona...
        price = weight * 18 / 1000  # El precio será igual al peso * 18
    else:  # De lo contrario...
        print(f'{zone} no es un código de zona válido.')  # Indicamos que el código no es válido
    print(f'El envío de tu paquete a la zona introducida costaría {price:.2f}€.')  # Mostramos lo que costaría
    # el envío del paquete a la zona indicada
else:  # De lo contrario...
    print('La entrega ha sido rechazada debido a que el peso del paquete supera los 5 kilos.')  # Indicamos
    # que el envío ha sido rechazado por exceder el peso límite
