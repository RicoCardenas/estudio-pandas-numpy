import numpy as np

numeros = np.array([1, 2, 3, 4, 5])
decimales = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
strings = np.array(["a", "b", "c", "d", "e"])
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([10, 20, 30, 40, 50])
filtro = c > 25

print(numeros)
print(type(numeros))
print("shape:", numeros.shape)
print("size:", numeros.size)
print("data type:", numeros.dtype)
print("data type decimales:", decimales.dtype)
print("data type strings:", strings.dtype)

print("Suma a + b:", a + b)
print("Multiplicacion a * b:", a * b)

print(filtro)
print(c[filtro])
print(c[(c > 10) & (c < 40)]) 