import numpy as np
import pandas as pd

# numeros = np.array([1.3, 1.4, .5, 2.4, 3.2, 4.1])


# print(numeros * 3)

# print(numeros < 2)

# print(numeros[numeros >= 2])



datos = {
    'ciudad' : [ 'Bogota', 'Medellin', 'Cali', 'Barranquilla'],
    'poblacion' : [ 7.4, 2.5, 2.2, 1.2],
    'area' : [ 1587, 380, 560, 154]
}

df = pd.DataFrame(datos)

# print(df)
# print(df[(df['area'] > 500) & (df['poblacion'] > 5)])
print(df.sort_values('poblacion'))
print(df.sort_values('poblacion', ascending=False))