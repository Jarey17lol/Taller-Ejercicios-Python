import pandas as pd
import codecs
import re

# Cargar dataset 
df = pd.read_csv("data/personas.csv")

# Limpiar profesion 
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

# Descifrar nombres 
def limpiar_y_descifrar(texto):
    if pd.isna(texto):
        return texto
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))
    texto = texto.strip()
    texto = codecs.decode(texto, 'rot_13')
    return texto.strip().title()

df["nombre"] = df["nombre_cifrado"].apply(limpiar_y_descifrar)

# Respuesta
resultado = df[(df["nombre"] == "Ana") & (df["profesion_limpia"] == "medico")]

print(f"¿Cuántos registros tienen nombre 'Ana' y son 'Medico'?: {len(resultado)}")
