# Descripción: Escribir un programa para calcular la nota final de un estudiante, considerando que:
# - cada respuesta correcta suma 5 puntos
# - cada respuesta incorrecta suma -1 puntos
# - cada respuesta en blanco suma 0 puntos.
#
# Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
#
# ¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes
# tipos de respuestas puedan cambiar en el futuro?
# Autor del ejercicio: Rafael Jiménez Cobos

correct_answers = int(input('Número de respuestas correctas: '))
incorrect_answers = int(input('Número de respuestas incorrectas: '))
blank_answers = int(input('Número de respuesta en blanco: '))

total_points = correct_answers*5+incorrect_answers*(-1)
mark = 0

if 0 <= total_points <= 4:
    mark = 0
if 5 <= total_points <= 9:
    mark = 1
if 10 <= total_points <= 14:
    mark = 2
if 15 <= total_points <= 19:
    mark = 3
if 20 <= total_points <= 24:
    mark = 4
if 25 <= total_points <= 29:
    mark = 5
if 30 <= total_points <= 34:
    mark = 6
if 35 <= total_points <= 39:
    mark = 7
if 40 <= total_points <= 44:
    mark = 8
if 45 <= total_points <= 49:
    mark = 9
if total_points == 50:
    mark = 10

print('La puntuación total del alumno es', total_points)
print('La nota final del alumno es', mark)
