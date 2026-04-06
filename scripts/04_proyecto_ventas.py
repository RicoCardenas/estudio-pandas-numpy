import pandas as pd

datos = {
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse", "Monitor", "Teclado"],
    "precio": [3000, 50, 120, 800, 3200, 45, 850, 130],
    "cantidad": [2, 10, 5, 3, 1, 8, 2, 4],
    "ciudad": ["Bogotá", "Bogotá", "Medellín", "Cali", "Medellín", "Cali", "Bogotá", "Cali"]
}

df = pd.DataFrame(datos)

df["total_venta"] = df["cantidad"] * df["precio"]

# print(df)

# print(df["total_venta"].sum())
# print(df["total_venta"].mean())
print(df["total_venta"].describe())

city_top = df.groupby('ciudad')["total_venta"].sum().sort_values(ascending=False)
print(city_top.head(1))