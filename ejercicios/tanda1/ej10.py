# Descripción: Un alumno desea saber cuál será su calificación final
# en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# * 55% del promedio de sus tres calificaciones parciales.
# * 30% de la calificación del examen final.
# * 15% de la calificación de un trabajo final.
# Autor del ejercicio: Rafael Jiménez Cobos

from statistics import mean
from math import ceil

par_cal1 = float(input('Introduce la calificación del primer parcial: '))
par_cal2 = float(input('Introduce la calificación del segundo parcial: '))
par_cal3 = float(input('Introduce la calificación del tercer parcial: '))
final_test_cal = float(input('Introduce la calificación del examen final: '))
final_assignment_cal = float(input('Introduce la calificación del trabajo final: '))
avg_cal = mean([par_cal1, par_cal2, par_cal3])
avg_cal_per = 55*avg_cal/100
final_test_cal_per = 30*final_test_cal/100
final_assignment_cal_per = 15*final_assignment_cal/100
final_cal = avg_cal_per+final_test_cal_per+final_assignment_cal_per

print('La nota final del alumno es', ceil(final_cal))
