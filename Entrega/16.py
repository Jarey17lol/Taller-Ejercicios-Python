import pandas as pd

# cargar dataset
df = pd.read_csv("data/personas.csv")

# convertir a string
df["salario_str"] = df["salario"].astype(str)

# reemplazos de letras confusas y eliminación de "aprox."
reemplazos = {
    "l": "1",
    "O": "0",
    "e": "3",
    "aprox.": ""
}

for old, new in reemplazos.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)

# reemplazar comas por puntos
df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)

# eliminar cualquier caracter que no sea digito o punto
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)

# convertir a float
df["salario_limpio"] = df["salario_limpio"].astype(float)

# calcular salario minimo
salario_minimo = df["salario_limpio"].min()

# resultado
print(round(salario_minimo, 0))