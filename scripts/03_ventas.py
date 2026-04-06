import pandas as pd


datos =  {
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse"],
    "precio": [3000, 50, 120, 800, 3200, 45],
    "cantidad": [2, 10, 5, 3, 1, 8],
    "ciudad": ["Bogotá", "Bogotá", "Medellín", "Cali", "Medellín", "Cali"]
}

df = pd.DataFrame(datos)

print(df)

df['total_venta'] = df['precio'] * df['cantidad']

print(df)

print(df.sort_values('total_venta', ascending = False).head(1))

df_total = df.groupby('ciudad')['total_venta'].sum()

print(df_total)

total_productos = df.groupby('producto')['total_venta'].sum().sort_values(ascending=False).head(1)

print(total_productos)



