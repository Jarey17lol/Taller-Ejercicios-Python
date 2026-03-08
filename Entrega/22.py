import pandas as pd
from datetime import datetime
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# función limpieza para fechas
def limpiar_fecha(fecha):
    if pd.isna(fecha):
        return None
    fecha = str(fecha).strip()
    fecha = re.sub(r'[^0-9\-/. ]', '', fecha)
    fecha = re.sub(r'[ /.]', '-', fecha)
    fecha = re.sub(r'^(\d{2})[ -](\d{2})', r'\1\2', fecha)
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)
    if match:
        y, m, d = match.groups()
        fecha = f"{y}-{int(m):02d}-{int(d):02d}"
    return fecha

# aplicar limpieza
df["fecha_nacimiento_limpia"] = df["fecha_nacimiento"].apply(limpiar_fecha)

# convertir a datetime
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')

# fecha actual
fecha_actual = pd.Timestamp('2026-02-26')

# calcular edad
df["edad"] = (fecha_actual - df["fecha_nacimiento_dt"]).dt.days // 365

# contar personas con mas de 50 años
cantidad_mas_50 = (df["edad"] > 50).sum()

# resultado
print(f"Cantidad de personas con más de 50 años: {cantidad_mas_50}")