# Descripción: 20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos)
# después de pedirnos cuantas monedas tenemos de 2 €, 1 €, 50 céntimos, 20 céntimos o 10 céntimos.
# Autor del ejercicio: Rafael Jiménez Cobos

two_e_coins = int(input('¿Cuantas monedas de 2€ tienes?'))
one_e_coins = int(input('¿Cuantas monedas de 1€ tienes?'))
fifty_c_coins = int(input('¿Cuantas monedas de 50c tienes?'))
twenty_c_coins = int(input('¿Cuantas monedas de 20c tienes?'))
ten_c_coins = int(input('¿Cuantas monedas de 10c tienes?'))

eur_calc = (two_e_coins*2)+one_e_coins
cent_calc = (fifty_c_coins*50)+(twenty_c_coins*20)+(ten_c_coins*10)
total_eur = eur_calc+(cent_calc//100)
total_cents = cent_calc % 100

print('Tenemos un total de', total_eur, 'euros y', total_cents, 'céntimos.')
