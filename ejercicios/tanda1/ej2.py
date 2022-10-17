# Descripción: Calcular el perímetro y área de un rectángulo dada su base y su altura.
# Autor del ejercicio: Rafael Jiménez Cobos

width = float(input('Introduce la base del rectángulo: '))
height = float(input('Introduce la altura del rectángulo: '))

perimeter = 2*(width+height)
area = width*height

print(f'El perímetro del rectángulo es {perimeter:.2f}, mientras que el área es {area:.2f}')
