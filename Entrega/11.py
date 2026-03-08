import pandas as pd
import re

# ── 1. Cargar dataset ──────────────────────────────────────────────
df = pd.read_csv("data/personas.csv")

# ── 2. Limpiar profesion (filtro mejorado) ────────────────────────
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

# ── 3. Respuesta pregunta 11 ──────────────────────────────────────
cantidad_unicas = df["profesion_limpia"].nunique()

print(f"¿Cuántas profesiones únicas existen después de normalizar?:{cantidad_unicas}")
