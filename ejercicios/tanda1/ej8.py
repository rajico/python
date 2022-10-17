# Descripción: Un vendedor recibe un sueldo base + un 10% extra por comisión
# de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
# por las tres ventas que realiza en el mes y el total que recibirá en el mes
# tomando en cuenta su sueldo base y comisiones.
# Autor del ejercicio: Rafael Jiménez Cobos

base_salary = float(input('Introduce el salario base del vendedor: '))
com = 10*base_salary/100
monthly_sales = 3
com_3_sales = com*monthly_sales
total = base_salary+com_3_sales

print('El vendedor ha obtenido', com_3_sales, 'euros en comisiones por tres ventas.')
print('El vendedor ha obtenido un total de', total, 'euros.')
