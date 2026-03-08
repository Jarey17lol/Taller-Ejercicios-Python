import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# funcion limpieza 
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

# convertir a datetime, ignorando errores
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')

# filtrar fechas entre 1990 y 2000 
inicio = pd.Timestamp('1990-01-01')
fin = pd.Timestamp('2000-12-31')
mask = (df["fecha_nacimiento_dt"] >= inicio) & (df["fecha_nacimiento_dt"] <= fin)

# contar registros
cantidad_1990_2000 = mask.sum()

# resultado
print(f"Cantidad de personas nacidas entre 1990 y 2000 (inclusive): {cantidad_1990_2000}")