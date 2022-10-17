# Variación del ejercicio 19 en la que utilizo variables constantes para resolver la pregunta.
# Autor del ejercicio: Rafael Jiménez Cobos

CORRECT_ANSWERS = 5
INCORRECT_ANSWERS = -1
BLANK_ANSWERS = 0

correct_questions = int(input('Número de preguntas correctas: '))
incorrect_questions = int(input('Número de preguntas incorrectas: '))
blank_questions = int(input('Número de preguntas en blanco: '))

total_answers = correct_questions+incorrect_questions+blank_questions
max_points = total_answers*CORRECT_ANSWERS

total_correct_answers = correct_questions*CORRECT_ANSWERS
total_incorrect_answers = incorrect_questions*INCORRECT_ANSWERS
total_blank_answers = blank_questions*BLANK_ANSWERS

total_points = total_correct_answers+total_incorrect_answers+total_blank_answers
points_percent = total_points*100//max_points

mark = points_percent*0.10

print('La nota es un total de', mark)
