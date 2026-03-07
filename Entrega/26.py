import pandas as pd
import codecs
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# --- Funciones de limpieza ---

# Ciudad: eliminar caracteres especiales y normalizar
def limpiar_texto(texto):
    texto = str(texto).strip()
    texto = re.sub(r'[^a-zA-Záéíóúñ ]', '', texto)
    return texto.lower()

df["ciudad"] = df["ciudad"].apply(limpiar_texto)

# Activo: normalizar a booleano
def limpiar_activo(valor):
    valor = str(valor).strip().lower()
    if valor in ["true", "yes", "1"]:
        return True
    return False

df["activo_bool"] = df["activo"].apply(limpiar_activo)

# Fecha de nacimiento: limpieza robusta
def limpiar_fecha(fecha):
    if pd.isna(fecha):
        return pd.NaT
    fecha = str(fecha).strip()
    fecha = re.sub(r'[^0-9\-/. ]', '', fecha)
    fecha = re.sub(r'[ /.]', '-', fecha)
    fecha = re.sub(r'^(\d{2})[ -](\d{2})', r'\1\2', fecha)
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)
    if match:
        y, m, d = match.groups()
        fecha = f"{y}-{int(m):02d}-{int(d):02d}"
    try:
        return pd.to_datetime(fecha, errors='coerce')
    except:
        return pd.NaT

df["fecha_nacimiento_dt"] = df["fecha_nacimiento"].apply(limpiar_fecha)

# --- Filtrado ---
mask = (
    (df["ciudad"] == "barranquilla") &
    (df["activo_bool"] == True) &
    (df["fecha_nacimiento_dt"] > pd.Timestamp('1980-12-31'))
)

cantidad_bq_activo_post1980 = mask.sum()

# Resultado
print(f"Cantidad de registros con ciudad 'Barranquilla', activos y nacidos después de 1980: {cantidad_bq_activo_post1980}")