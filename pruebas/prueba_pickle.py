"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 21/12/22
"""

# Importa módulo pickle
import pickle

# Declara lista
lista = ['Perl', 'Python', 'Ruby']

# Abre archivo binario para escribir
archivo = open('pruebas', 'wb')

# Escribe lista en archivo
pickle.dump(lista, archivo)

# Cierra archivo
archivo.close()

archivo = open('pruebas', 'wb')

# Añado PHP
lista.append('PHP')

pickle.dump(lista, archivo)

archivo.close()

# Borra de memoria la lista
del lista

# Abre archivo binario para leer
archivo = open('pruebas', 'rb')

# carga lista desde archivo
lista = pickle.load(archivo)

# Muestra lista
print(lista)

# Cierra archivo
archivo.close()
