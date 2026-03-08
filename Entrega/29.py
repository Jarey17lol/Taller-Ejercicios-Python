import pandas as pd
import re

# Cargar dataset 
df = pd.read_csv("data/personas.csv")

# Limpiar email 
def limpiar_email(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()
    texto = texto.lower()
    texto = re.sub(r'^mailto:', '', texto)
    texto = re.sub(r'[()<>]', '', texto)
    texto = re.sub(r'\s*@\s*', '@', texto)
    texto = re.sub(r'\s*\.\s*', '.', texto)
    texto = re.sub(r'@mail\.com$', '@gmail.com', texto)
    return texto.strip()

df["email_limpio"] = df["email"].apply(limpiar_email)

# Respuesta
cantidad = df["email_limpio"].str.endswith("@gmail.com").sum()

print(f"¿Cuántos registros tienen email con dominio 'gmail.com'?: {cantidad}")
