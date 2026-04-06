import pandas as pd

datos = {
    "nombre": ["Ana", "Luis", "Carlos", "Sofia"],
    "edad": [20, 25, 30, 22],
    "nota": [4.5, 3.8, 4.2, 4.9]
}

df = pd.DataFrame(datos)

# print(df)
# print(df["nombre"])
# print(df[df["edad"] > 23])
# print(df["edad"] > 23)

# print(df.sort_values("nota", ascending=False).head(2)) 
# print(df.sort_values("edad", ascending=False).head(2))
# print(df[df["edad"]>21].sort_values("nota", ascending=False).head(2))
# print(df.loc[0, "nombre"])
# print (df.iloc[0:2, 0])
# print(df.iloc[2])
# df.iloc[2, 2] = 5.0
# print(df)
# df.loc[0, "edad"] = 21
# print(df)
# df["aprobado"] = df["nota"] >= 4.0
# print(df)
# print(df[df["aprobado"] == True])
# df["nota_base_10"] = df["nota"] * 2
# print(df)
# df = df.drop(["nota_base_10"], axis=1)
# print(df)

datos_null = {
    'Nombre' : ['Julian', 'Juana', 'Alejandro', 'Gabriela'],
    'Edad' : [28, 32, None, 25],
    'Nota' : [4.5, None, 3.8, 4.2]
}

df_null = pd.DataFrame(datos_null)

print(df_null)
print(df_null.isnull().sum())
print(df_null.dropna())