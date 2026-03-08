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

# ── 3. Descifrar nombres con ROT13 ────────────────────────────────
def limpiar_y_descifrar(texto):
    if pd.isna(texto):
        return texto
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))
    texto = texto.strip()
    texto = codecs.decode(texto, 'rot_13')
    return texto.strip().title()

df["nombre"] = df["nombre_cifrado"].apply(limpiar_y_descifrar)

# ── 4. Respuesta pregunta 23 ──────────────────────────────────────
resultado = df[(df["nombre"] == "Carlos") & (df["ciudad"] == "Cali")]
print(f"¿Cuántos registros tienen nombre Carlos y viven en Cali?: {len(resultado)}")
