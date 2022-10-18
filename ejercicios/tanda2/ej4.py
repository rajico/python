"""
Nombre del programa: División de números con aviso por 0
Enunciado: Crea un programa que pida al usuario dos números y muestre su división
si el segundo no es cero, o un mensaje de aviso en caso contrario.
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 14/10/22
"""

num1 = int(input('Introduce el primer número: '))  # Pedimos al usuario introducir el primer número
num2 = int(input('Introduce el segundo número: '))  # Pedimos al usuario introducir el segundo número

if num2 > 0:  # Si el segundo número es mayor que 0...
    div = num1 // num2  # Almacenamos en una variable la división entre los dos números
    print(f'El resultado de la división entre {num1} y {num2} es {div}.')  # Y mostramos por pantalla el resultado
else:  # De lo contrario
    print(f'¡AVISO! No puedes dividir entre 0.')  # Mostramos un aviso
