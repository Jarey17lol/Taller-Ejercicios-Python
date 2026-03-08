import pandas as pd
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

# ── 3. Limpiar profesion (filtro mejorado) ────────────────────────
def limpiar_profesion(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)
    return texto.strip().lower()

df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# ── 4. Respuesta pregunta 27 ──────────────────────────────────────
ingenieros = df[df["profesion_limpia"] == "ingeniero"]
ciudad_top = ingenieros["ciudad"].value_counts().idxmax()
cantidad = ingenieros["ciudad"].value_counts().max()

print(f"¿Cuál es la ciudad con más 'Ingenieros'?: {ciudad_top} con {cantidad} ingenieros")

