import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# guardar columnas originales
df["profesion_original"] = df["profesion"]
df["ciudad_original"] = df["ciudad"]

# Función de limpieza
def limpiar_texto(texto):
    texto = str(texto).strip()
    texto = re.sub(r'[^a-zA-Záéíóúñ ]', '', texto)
    return texto.lower()

# aplicar limpieza
df["profesion"] = df["profesion"].apply(limpiar_texto)
df["ciudad"] = df["ciudad"].apply(limpiar_texto)

# mostrar tabla de comparación
tabla_comparacion = df[["profesion_original", "profesion", "ciudad_original", "ciudad"]].head(100)
print(tabla_comparacion)