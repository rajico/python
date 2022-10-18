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

grape_type = input('Introduce el tipo de uva, A ó B: ').upper()  # Indicamos al usuario introducir el tipo de
# uva, almacenando el valor introducido en mayúsculas
grape_size = int(input('Introduce el tamaño de uva, 1 ó 2: '))  # Indicamos al usuario introducir el tamaño de uva
kg_price = float(input('Introduce el precio inicial para el kilo de uvas: '))  # Indicamos al usuario introducir
# el precio inicial en kg
final_price = 0  # Creamos la variable donde almacenaremos el precio final

if grape_type == 'A':  # Si el tipo de uva es A...
    if grape_size == 1:  # Y además el tamaño es exactamente igual a 1...
        final_price = kg_price + 0.20  # El precio final es igual al precio inicial + un incremento de 0.20
    elif grape_size == 2:  # O el tamaño es exactamente igual a 2...
        final_price = kg_price + 0.30  # El precio final es igual al precio inicial + un incremento de 0.30
    else:  # De lo contrario...
        print(f'{grape_size} no es un tamaño de uva admitido.')  # Indicamos que el tamaño introducido no es válido
    print(
        f'El precio final teniendo en cuenta que el tipo es {grape_type} y el tamaño '
        f'es {grape_size}, es de {final_price:.2f} €/kg.')  # Mostramos por pantalla el precio final
elif grape_type == 'B':  # Si el tipo de uva es B...
    if grape_size == 1:  # Y además el tamaño es exactamente igual a 1...
        final_price = kg_price - 0.30  # El precio final es igual al precio inicial - una rebaja de 0.30
    elif grape_size == 2:  # Y además el tamaño es exactamente igual a 2...
        final_price = kg_price - 0.50  # El precio final es igual al precio inicial - una rebaja de 0.50
    else:  # De lo contrario...
        print(f'{grape_size} no es un tamaño de uva admitido.')  # Indicamos que el tamaño introducido no es válido
    print(
        f'El precio final teniendo en cuenta que el tipo es {grape_type} y el tamaño '
        f'es {grape_size}, es de {final_price:.2f} €/kg.')  # Mostramos por pantalla el precio final
else:  # De lo contrario...
    print(f'{grape_type} no es un tipo de uva admitido.')  # Indicamos que el tipo introducido no es válido
