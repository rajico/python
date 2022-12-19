"""
Nombre del programa: Calcular precio a pagar
Descripción: Una persona adquirió un producto para pagar en 20 meses.
El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente.
Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después
de los 20 meses.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 22/10/22
"""

pay_count = 10
total = 0

for i in range(1, 20+1):
    print(f'Mes {i}, paga: {pay_count}€.')
    pay_count = pay_count * 2
    total += pay_count

print(f'\nEl total a pagar es de {total}€.')
