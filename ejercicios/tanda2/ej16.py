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

call_duration = int(input('Introduce la duración de llamada en MINUTOS: '))
call_day = input('¿Qué día se realizó la llamada? ').lower()
price = 0
final_price = 0

if call_day == 'domingo':
    if 1 <= call_duration <= 5:
        price = call_duration
        extra = (3 * price) / 100
        final_price = price + extra
    elif 6 <= call_duration <= 8:
        dif = abs(5 - call_duration)
        price = dif * 0.80 + 5
        extra = (3 * price) / 100
        final_price = price + extra
    elif 9 <= call_duration <= 10:
        dif = abs(8 - call_duration)
        price = dif * 0.70 + 7.40
        extra = (3 * price) / 100
        final_price = price + extra
    elif call_duration > 10:
        dif = abs(10 - call_duration)
        price = dif * 0.50 + 8.80
        extra = (3 * price) / 100
        final_price = price + extra
    print(f'El coste de una llamada de {call_duration} minutos es de {final_price:.2f}€.')
elif call_day != 'domingo':
    call_turn = input('¿En qué turno se realizó la llamada, mañana o tarde? ').lower()
    if call_turn == 'mañana':
        if 1 <= call_duration <= 5:
            price = call_duration
            extra = (15 * price) / 100
            final_price = price + extra
        elif 6 <= call_duration <= 8:
            dif = abs(5 - call_duration)
            price = dif * 0.80 + 5
            extra = (15 * price) / 100
            final_price = price + extra
        elif 9 <= call_duration <= 10:
            dif = abs(8 - call_duration)
            price = dif * 0.70 + 7.40
            extra = (15 * price) / 100
            final_price = price + extra
        elif call_duration > 10:
            dif = abs(10 - call_duration)
            price = dif * 0.50 + 8.80
            extra = (15 * price) / 100
            final_price = price + extra
        print(f'El coste de una llamada de {call_duration} minutos es de {final_price:.2f}€.')
    elif call_turn == 'tarde':
        if 1 <= call_duration <= 5:
            price = call_duration
            extra = (10 * price) / 100
            final_price = price + extra
        elif 6 <= call_duration <= 8:
            dif = abs(5 - call_duration)
            price = dif * 0.80 + 5
            extra = (10 * price) / 100
            final_price = price + extra
        elif 9 <= call_duration <= 10:
            dif = abs(8 - call_duration)
            price = dif * 0.70 + 7.40
            extra = (10 * price) / 100
            final_price = price + extra
        elif call_duration > 10:
            dif = abs(10 - call_duration)
            price = dif * 0.50 + 8.80
            extra = (10 * price) / 100
            final_price = price + extra
        print(f'El coste de una llamada de {call_duration} minutos es de {final_price}€.')
    else:
        print(f'{call_turn} no es un turno válido.')
