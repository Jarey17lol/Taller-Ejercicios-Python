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

# Limpiar ciudades
df["ciudad"] = df["ciudad"].apply(limpiar_texto)

# Filtrar registros con nombre "carlos" y ciudad "cali"
mask = (df["nombre"] == "carlos") & (df["ciudad"] == "cali")

# Contar registros
cantidad_carlos_cali = mask.sum()

# Mostrar resultado
print(f"Cantidad de registros con nombre 'Carlos' y ciudad 'Cali': {cantidad_carlos_cali}")