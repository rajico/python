# Descripción: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
# desea saber cuanto deberá pagar finalmente por su compra.
# Autor del ejercicio: Rafael Jiménez Cobos

i_price = float(input('Introduce el precio inicial de la compra: '))
disc = 15*i_price/100
f_price = i_price-disc

print('El cliente debe pagar un total de', f_price, 'euros.')
