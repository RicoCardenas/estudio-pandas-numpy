import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/ventas.csv')

# print(df.head())

df['total_venta'] = df['cantidad'] * df['precio']

# print(df.head())

df['fecha'] = pd.to_datetime(df['fecha'])

# print(df.head())

ventas_ciudad = df.groupby('ciudad')['total_venta'].sum()
print(ventas_ciudad)

ventas_ciudad.plot(kind = 'bar')

plt.title("Ventas por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Total Ventas")

plt.tight_layout()
plt.savefig("img/ventas_por_ciudad.png")
plt.close()

ventas_producto = df.groupby('producto')['total_venta'].sum().sort_values(ascending=False)

ventas_producto.plot(kind = 'bar')

plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Total Ventas")

plt.tight_layout()
plt.savefig("img/ventas_por_producto.png")
plt.close()

ventas_fecha = df.groupby('fecha')['total_venta'].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
ventas_fecha.plot(kind = 'line', marker='o')

plt.title("Ventas por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Total Ventas")

plt.tight_layout()
plt.savefig("img/ventas_por_fecha.png")
plt.close()