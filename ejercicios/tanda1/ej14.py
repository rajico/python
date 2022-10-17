# Descripción: Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.
# Autor del ejercicio: Rafael Jiménez Cobos

# num = int(input('Introduce un número de dos cifras: '))

original_number = int(input('Introduce un número : '))
lst_number = list(str(original_number))
lst_number.reverse()
reversed_number = ''.join(lst_number)

print(reversed_number)
