"""
LAST_PAIR = 200

print('fPrimeros {LAST_PAIR // 2} números')
print('----------------------------------')

pair = 2

while pair <= LAST_PAIR:
    print(f'Par número {pair // 2}: {pair}')
    pair += 2


////////////////////////////////

Ejemplo de Repetir

NUM_PAIR = 100

print('fPrimeros {NUM_PAIR} números')
print('----------------------------------')

n = 0

while True:
    n += 1
    print(f'Par número {n:03}: {n * 2}')
    if n == NUM_PAIR:
        break

"""

print('Programa que pide cadenas y las almacena en una lista\n')

string = input('Introduce una cadena: ')  # Introducimos una cadena por pantalla
string_list = []  # Creamos una lista vacía donde almacenaremos las cadenas introducidas
index = 0  # Creamos un índice con valor 0 para el bucle for

while string != '':  # Mientras que la cadena no esté vacía
    string_list.append(string)  # Añadimos la cadena introducida a la lista
    string = input('Introduce una cadena: ')  # Volvemos a pedir una cadena hasta que esté vacía
for i in string_list:  # Bucle for por cada elemento de la lista de cadenas
    print(f'Elemento {index}: {string_list[index]}')  # Mostramos por pantalla el número del elemento y
    # el valor que corresponde a ese número
    index += 1  # Sumamos 1 al índice para sacar el siguiente elemento
