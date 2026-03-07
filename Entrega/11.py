import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# limpiar caracteres especiales
df["profesion_limpia"] = df["profesion"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)

# eliminar espacios y normalizar a minúsculas
df["profesion_limpia"] = df["profesion_limpia"].str.strip().str.lower()

# contar profesiones únicas
profesiones_unicas = df["profesion_limpia"].nunique()

print("Cantidad de profesiones únicas después de normalizar:", profesiones_unicas)