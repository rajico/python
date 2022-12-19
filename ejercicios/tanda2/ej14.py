"""
Nombre del programa: Venta de uvas
Enunciado: La asociación de vinicultores tiene como política fijar un precio inicial al
kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2.
Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño,
se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque,
considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1;
y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

grape_type = input('Introduce el tipo de uva, A ó B: ').upper()
grape_size = int(input('Introduce el tamaño de uva, 1 ó 2: '))
kg_price = float(input('Introduce el precio inicial para el kilo de uvas: '))
final_price = 0

if grape_type == 'A':
    if grape_size == 1:
        final_price = kg_price + 0.20
    elif grape_size == 2:
        final_price = kg_price + 0.30
    else:
        print(f'{grape_size} no es un tamaño de uva admitido.')
    print(
        f'El precio final teniendo en cuenta que el tipo es {grape_type} y el tamaño '
        f'es {grape_size}, es de {final_price:.2f} €/kg.')
elif grape_type == 'B':
    if grape_size == 1:
        final_price = kg_price - 0.30
    elif grape_size == 2:
        final_price = kg_price - 0.50
    else:
        print(f'{grape_size} no es un tamaño de uva admitido.')
    print(
        f'El precio final teniendo en cuenta que el tipo es {grape_type} y el tamaño '
        f'es {grape_size}, es de {final_price:.2f} €/kg.')
else:
    print(f'{grape_type} no es un tipo de uva admitido.')
