import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# limpiar caracteres extra y espacios
df["activo_str"] = df["activo"].astype(str).str.strip()
df["activo_str"] = df["activo_str"].str.replace(r'[^a-zA-Z0-9áéíóúñ]', '', regex=True)

# normalizar a minusculas
df["activo_str"] = df["activo_str"].str.lower()

# mapear valores conocidos a booleano
df["activo_bool"] = df["activo_str"].map({
    "true": True,
    "1": True,
    "si": True,
    "sí": True,
    "s": True,
    "yes": True,
    "false": False,
    "0": False,
    "no": False,
    "n": False
}).fillna(False)

# contar registros con activo False
cantidad_activo_false = (~df["activo_bool"]).sum()

# resultado
print(f"Cantidad de registros con activo=False: {cantidad_activo_false}")