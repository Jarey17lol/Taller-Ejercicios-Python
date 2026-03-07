import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# limpiar caracteres especiales
df["profesion_limpia"] = df["profesion"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)

# eliminar espacios y convertir a minúsculas
df["profesion_limpia"] = df["profesion_limpia"].str.strip().str.lower()

# contar registros con profesión "ingeniero"
cantidad_ingenieros = (df["profesion_limpia"] == "ingeniero").sum()

print("Registros con profesión Ingeniero después de limpiar:", cantidad_ingenieros)