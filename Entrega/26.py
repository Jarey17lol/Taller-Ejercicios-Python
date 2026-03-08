import pandas as pd
import codecs
import re

# ── 1. Cargar dataset ──────────────────────────────────────────────
df = pd.read_csv("data/personas.csv")

# ── 2. Limpiar y corregir ciudades ────────────────────────────────
correcciones_ciudades = {
    "S@nt@ M@rt@": "Santa Marta", "V@ll3dup@r": "Valledupar",
    "M@niz@l3s": "Manizales", "Sinc3l3jo": "Sincelejo",
    "Buc@r@m@ng@": "Bucaramanga", "Tunj@": "Tunja",
    "Ib@gu3": "Ibague", "C@rt@g3n@": "Cartagena",
    "Arm3ni@": "Armenia", "M3d3llin": "Medellin",
    "Cucut@": "Cucuta", "C@li": "Cali",
    "P3r3ir@": "Pereira", "Mont3ri@": "Monteria",
    "Bogot@": "Bogota", "Vill@vic3ncio": "Villavicencio",
    "N3iv@": "Neiva", "Pop@y@n": "Popayan",
    "B@rr@nquill@": "Barranquilla", "P@sto": "Pasto"
}

df["ciudad"] = df["ciudad"].str.strip()
df["ciudad"] = df["ciudad"].replace(correcciones_ciudades)
df["ciudad"] = df["ciudad"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)
df["ciudad"] = df["ciudad"].str.strip().str.title()

# ── 3. Limpiar columna activo ─────────────────────────────────────
df["activo_str"] = df["activo"].astype(str).str.strip()
df["activo_str"] = df["activo_str"].str.replace(r'[^a-zA-Z0-9áéíóúñ]', '', regex=True)
df["activo_str"] = df["activo_str"].str.lower()

df["activo_bool"] = df["activo_str"].map({
    "true": True,  "1": True,  "si": True,
    "sí": True,    "s": True,  "yes": True,
    "false": False, "0": False, "no": False, "n": False
}).fillna(False)

# ── 4. Limpiar fecha de nacimiento ────────────────────────────────
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

df["fecha_nacimiento_limpia"] = df["fecha_nacimiento"].apply(limpiar_fecha)
df["fecha_nacimiento_dt"] = pd.to_datetime(df["fecha_nacimiento_limpia"], errors='coerce')

# ── 5. Respuesta pregunta 26 ──────────────────────────────────────
limite = pd.Timestamp('1980-12-31')

resultado = df[
    (df["ciudad"] == "Barranquilla") &
    (df["activo_bool"] == True) &
    (df["fecha_nacimiento_dt"] > limite)
]

print(f"¿Cuántos registros tienen ciudad 'Barranquilla', activos y nacidos después de 1980?:{len(resultado)}")

