"""
Nombre del programa: Pago por llamada
Enunciado: La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que esta dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto,
los siguientes tres, 80 céntimos por minuto, los siguientes dos minutos, 70 céntimos por minuto, y a partir
del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en
turno de tarde, 10%. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona
que realiza una llamada.

Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 16/10/22
"""

call_duration = int(input('Introduce la duración de llamada en MINUTOS: '))  # Indicamos al usuario introducir
# la duración de la llamada
call_day = input('¿Qué día se realizó la llamada? ').lower()  # Indicamos al usuario introducir el día en el que
# se realizó la llamada
price = 0  # Creamos la variable donde almacenaremos el precio inicial
final_price = 0  # Creamos la variable donde almacenaremos el precio final

if call_day == 'domingo':  # Si el día en el que se realizó la llamada fue un domingo...
    if 1 <= call_duration <= 5:  # Si la duración de la llamada fue entre 1 y 5 minutos...
        price = call_duration  # El precio inicial es igual al tiempo de llamada, ya que los 5 primeros
        # minutos se cobran a 1/minuto
        extra = (3 * price) / 100  # Como es domingo, se cobra un extra del 3%
        final_price = price + extra  # El precio final será igual al precio + el extra
    elif 6 <= call_duration <= 8:  # Si la duración de la llamada fue entre 6 y 8 minutos...
        dif = abs(5 - call_duration)  # Calculamos la diferencia entre 5 y el tiempo de llamada
        price = dif * 0.80 + 5  # El precio inicial es igual a la diferencia por 0.80
        # (lo que se cobra entre 6 y 8 minutos de llamada) + 5 (los 5 € cobrados por los 5 primeros minutos)
        extra = (3 * price) / 100  # Como es domingo, se cobra un extra del 3%
        final_price = price + extra  # El precio final será igual al precio + el extra
    elif 9 <= call_duration <= 10:  # Si la duración de la llamada fue entre 9 y 10 minutos...
        dif = abs(8 - call_duration)  # Calculamos la diferencia entre 8 y el tiempo de llamada
        price = dif * 0.70 + 7.40  # El precio inicial es igual a la diferencia por 0.70
        # (lo que se cobra entre 9 y 10 minutos de llamada) + 7.40 (cobrados por los 8 primeros minutos)
        extra = (3 * price) / 100  # Como es domingo, se cobra un extra del 3%
        final_price = price + extra  # El precio final será igual al precio + el extra
    elif call_duration > 10:  # Si la duración de la llamada fue superior a 10 minutos...
        dif = abs(10 - call_duration)  # Calculamos la diferencia entre 10 y el tiempo de llamada
        price = dif * 0.50 + 8.80  # El precio inicial es igual a la diferencia por 0.50
        # (lo que se cobra a partir de los 10 minutos de llamada) + 8.80 (cobrados por los 10 primeros minutos)
        extra = (3 * price) / 100  # Como es domingo, se cobra un extra del 3%
        final_price = price + extra  # El precio final será igual al precio + el extra
    print(f'El coste de una llamada de {call_duration} minutos es de {final_price:.2f}€.')  # Mostramos el precio
    # final en función del tiempo de llamada
elif call_day != 'domingo':  # Si el día de la llamada no fue un domingo...
    call_turn = input('¿En qué turno se realizó la llamada, mañana o tarde? ').lower()  # Indicamos al usuario
    # introducir el turno en el que se realizó la llamada
    if call_turn == 'mañana':  # Si fue el turno de mañana...
        if 1 <= call_duration <= 5:  # Si la duración de llamada fue entre 1 y 5 minutos...
            price = call_duration  # El precio inicial es igual al tiempo de llamada
            extra = (15 * price) / 100  # Al ser turno de mañana, se cobra un extra del 15%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif 6 <= call_duration <= 8:  # Si la duración de llamada fue entre 6 y 8 minutos...
            dif = abs(5 - call_duration)  # Calculamos la diferencia entre 5 y el tiempo de llamada
            price = dif * 0.80 + 5  # El precio inicial es igual a la diferencia * 0.80 + 5
            extra = (15 * price) / 100  # Al ser turno de mañana, se cobra un extra del 15%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif 9 <= call_duration <= 10:  # Si la duración de llamada fue entre 9 y 10 minutos...
            dif = abs(8 - call_duration)  # Calculamos la diferencia entre 8 y el tiempo de llamada
            price = dif * 0.70 + 7.40  # El precio inicial es igual a la diferencia * 0.70 + 7.40
            extra = (15 * price) / 100  # Al ser turno de mañana, se cobra un extra del 15%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif call_duration > 10:  # Si la duración de la llamada fue superior a 10 minutos...
            dif = abs(10 - call_duration)  # Calculamos la diferencia entre 10 y el tiempo de llamada
            price = dif * 0.50 + 8.80  # El precio inicial es igual a la diferencia * 0.50 + 8.80
            extra = (15 * price) / 100  # Al ser turno de mañana, se cobra un extra del 15%
            final_price = price + extra  # El precio final será igual al precio + el extra
        print(f'El coste de una llamada de {call_duration} minutos es de {final_price:.2f}€.')  # Mostramos el precio
        # final en función del tiempo de llamada
    elif call_turn == 'tarde':  # Si, por el contrario, fue el turno de tarde...
        if 1 <= call_duration <= 5:  # Si la duración de llamada fue entre 1 y 5 minutos...
            price = call_duration  # El precio inicial es igual al tiempo de llamada
            extra = (10 * price) / 100  # Al ser turno de tarde, se cobra un extra del 10%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif 6 <= call_duration <= 8:  # Si la duración de llamada fue entre 6 y 8 minutos...
            dif = abs(5 - call_duration)  # Calculamos la diferencia entre 5 y el tiempo de llamada
            price = dif * 0.80 + 5  # El precio inicial es igual a la diferencia * 0.80 + 5
            extra = (10 * price) / 100  # Al ser turno de tarde, se cobra un extra del 10%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif 9 <= call_duration <= 10:  # Si la duración de llamada fue entre 9 y 10 minutos...
            dif = abs(8 - call_duration)  # Calculamos la diferencia entre 8 y el tiempo de llamada
            price = dif * 0.70 + 7.40  # El precio inicial es igual a la diferencia * 0.70 + 7.40
            extra = (10 * price) / 100  # Al ser turno de tarde, se cobra un extra del 10%
            final_price = price + extra  # El precio final será igual al precio + el extra
        elif call_duration > 10:  # Si la duración de la llamada fue superior a 10 minutos...
            dif = abs(10 - call_duration)  # Calculamos la diferencia entre 10 y el tiempo de llamada
            price = dif * 0.50 + 8.80  # El precio inicial es igual a la diferencia * 0.50 + 8.80
            extra = (10 * price) / 100  # Al ser turno de tarde, se cobra un extra del 10%
            final_price = price + extra  # El precio final será igual al precio + el extra
        print(f'El coste de una llamada de {call_duration} minutos es de {final_price}€.')  # Mostramos el precio final
        # en función del tiempo de llamada
    else:  # De lo contrario...
        print(f'{call_turn} no es un turno válido.')  # Indicamos que el turno no es válido
