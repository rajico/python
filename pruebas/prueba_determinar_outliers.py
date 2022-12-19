"""
Nombre del programa: Determinar Outliers
Descripción: Script que determina los Outliers de una muestra de población normal
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 8/11/22
"""

import numpy as np
import scipy.stats as st

mu, sigma = 50, 10  # media y desviación típica de la población

# Generamos una muestra de tamaño 100
datos = np.random.normal(mu, sigma, 100)

# Cambiamos los valores de dos datos para convertirlos en outliers
datos[50] = 100
datos[75] = 1

print(datos)

# CRITERIO 1: PROBABILIDAD GLOBAL
# probabilidad de la muestra de estar dentro de las bandas
p_g = 0.95
# probabilidad global de una cola
alfa_g = (1-p_g)/2
# probabilidad  de las colas para un solo dato
alfa = 1-(1-alfa_g)**(1/len(datos))

# CRITERIO 2: Criterio Chauvenet
# alfa=1/(2*len(datos))
Z_alfa = st.norm.ppf(1-alfa/2)
# Impresión de resultados
alfa = round(alfa, 5)
Z_alfa = round(Z_alfa, 5)
print(f" Alfa ={alfa}")
print(f"Cuantil Z_(1-alfa/2) = {Z_alfa}")

xL = round(np.mean(datos)-Z_alfa * np.std(datos), 4)
xU = round(np.mean(datos)+Z_alfa * np.std(datos), 4)
print(f" Banda= [ {xL}, {xU}]")

for i in range(len(datos)):
    if datos[i] < xL or datos[i] > xU:
        print(f" El dato[{i}] = {datos[i]} es un outlier")

Q1 = np.quantile(datos, 0.25)
Q3 = np.quantile(datos, 0.75)
IQR = Q3 - Q1
k = 1.5
xL = Q1 - k * IQR
xU = Q3 + k * IQR
for i in range(len(datos)):
    if datos[i] < xL or datos[i] > xU:
        print(f" El dato[{i}] = {datos[i]} es un outlier")
