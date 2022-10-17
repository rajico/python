# Descripción: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
# Autor del ejercicio: Rafael Jiménez Cobos

num1 = int(input('Dime el primer número: '))
num2 = int(input('Dime el segundo número: '))

sum_num = num1+num2
sub_num = num1-num2
div_num = num1/num2
mul_num = num1*num2

print('La suma de', num1, 'mas', num2, 'es:', sum_num)
print('La resta de', num1, 'menos', num2, 'es:', sub_num)
print('La división de', num1, 'entre', num2, 'es:', div_num)
print('La multiplicación de', num1, 'por', num2, 'es:', mul_num)
