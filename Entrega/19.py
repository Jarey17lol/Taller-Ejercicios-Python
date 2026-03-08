import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# convertir a string
df["fecha_nacimiento_str"] = df["fecha_nacimiento"].astype(str).str.strip()

# patron para YYYY-MM-DD
patron = r'^\d{4}-\d{2}-\d{2}$'

# detectar registros que no cumplen el patron
fechas_incorrectas = ~df["fecha_nacimiento_str"].str.match(patron)

# contar registros con formato diferente
cantidad_fechas_incorrectas = fechas_incorrectas.sum()

# resultado
print(f"Cantidad de registros con fecha de nacimiento con formato diferente a YYYY-MM-DD: {cantidad_fechas_incorrectas}")