# Calculamos x en una ecuación de primer grado: ax + b = 0

try:
    a = int(input('Dame valor de a: '))
    b = int(input('Dame valor de b: '))

    x = -b/a

    print(f'El valor de x en la ecuación {a}x + {b} = 0 es {x:.2f}')

except ZeroDivisionError:
    print('No puedes poner un cero como valor de a.')

except ValueError:
    print('Los valores de a y b deben ser numéricos enteros.')
