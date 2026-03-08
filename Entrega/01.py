import pandas as pd

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Limpieza de id
ids_no_numericos = df["id"].astype(str).str.contains(r"\D")

# contar filas
cantidad = ids_no_numericos.sum()

print("Filas con id no numérico:", cantidad)