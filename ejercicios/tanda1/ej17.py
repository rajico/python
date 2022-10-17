# Descripción: Un ciclista parte de una ciudad 'A' a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
# Autor del ejercicio: Rafael Jiménez Cobos

hour_start = int(input('Introduce la hora de salida: '))
minutes_start = int(input('Introduce los minutos de salida: '))
seconds_start = int(input('Introduce los segundos de salida: '))
seconds_time = int(input('Introduce los segundos que tarda el ciclista: '))
hour_to_seconds = hour_start*3600
minutes_to_seconds = minutes_start*60
start_time_in_seconds = hour_to_seconds+minutes_to_seconds+seconds_start
total_time_in_seconds = start_time_in_seconds+seconds_time
seconds_to_hour = int(total_time_in_seconds/3600)
seconds_to_minutes = int((total_time_in_seconds-(seconds_to_hour*3600))/60)
seconds = total_time_in_seconds-((seconds_to_hour*3600)+(seconds_to_minutes*60))

print('La hora de llegada es de', seconds_to_hour, 'horas,', seconds_to_minutes, 'minutos y', seconds, 'segundos.')
