# Descripción: Un vendedor recibe un sueldo base + un 10% extra por comisión
# de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
# por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones.
# Autor del ejercicio: Rafael Jiménez Cobos

COMMISSION = 10

base_salary = float(input('Introduce el salario base del vendedor: '))
sale1 = float(input('Introduce el dinero obtenido por la primera venta: '))
sale2 = float(input('Introduce el dinero obtenido por la segunda venta: '))
sale3 = float(input('Introduce el dinero obtenido por la tercera venta: '))

com1 = COMMISSION * sale1 / 100
com2 = COMMISSION * sale2 / 100
com3 = COMMISSION * sale3 / 100

total_commissions = com1 + com2 + com3
total_gained = base_salary + total_commissions

print(f'El vendedor ha obtenido {total_commissions:.2f} € en comisiones por tres ventas.')
print(f'El vendedor ha obtenido un total de {total_gained:.2f} €.')
