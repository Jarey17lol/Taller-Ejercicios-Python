import pandas as pd
import codecs

# cargar dataset
df = pd.read_csv("data/personas.csv")

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# limpiar y normalizar
df["nombre"] = df["nombre"].str.strip().str.title()

# obtener nombre mas frecuente
nombre_mas_frecuente = df["nombre"].value_counts().idxmax()
cantidad = df["nombre"].value_counts().max()

print("Nombre más frecuente:", nombre_mas_frecuente)
print("Cantidad de veces:", cantidad)