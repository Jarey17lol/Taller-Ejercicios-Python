import pandas as pd
import codecs
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Función para limpiar texto: elimina caracteres especiales y espacios extra, devuelve en minúsculas
def limpiar_texto(texto):
    texto = str(texto).strip()                       # quitar espacios
    texto = re.sub(r'[^a-zA-Záéíóúñ ]', '', texto)  # eliminar caracteres especiales
    texto = texto.lower()                            # pasar a minúsculas
    return texto

# Decodificar y limpiar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: limpiar_texto(codecs.decode(str(x), 'rot_13')))

# Limpiar profesiones
df["profesion"] = df["profesion"].apply(limpiar_texto)

# Filtrar registros con nombre "ana" y profesión "medico"
mask = (df["nombre"] == "ana") & (df["profesion"] == "medico")

# Contar registros
cantidad_ana_medico = mask.sum()

# Mostrar resultado
print(f"Cantidad de registros con nombre 'Ana' y profesión 'Medico': {cantidad_ana_medico}")