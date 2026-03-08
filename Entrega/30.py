import pandas as pd
import codecs
import re

# Cargar dataset 
df = pd.read_csv("data/personas.csv")

# Descifrar nombres y apellidos 
def limpiar_y_descifrar(texto):
    if pd.isna(texto):
        return texto
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))
    texto = texto.strip()
    texto = codecs.decode(texto, 'rot_13')
    return texto.strip().title()

df["nombre"]   = df["nombre_cifrado"].apply(limpiar_y_descifrar)
df["apellido"] = df["apellido_cifrado"].apply(limpiar_y_descifrar)

# Respuesta
resultado = df[(df["nombre"] == "Jose") & (df["apellido"] == "Garcia")]

print(f"Pregunta 30: ¿Cuántos registros tienen nombre 'Jose' y apellido 'Garcia'?")
print(f"Respuesta 30: {len(resultado)}")