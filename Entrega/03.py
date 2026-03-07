import pandas as pd
import codecs

# cargar dataset
df = pd.read_csv("data/personas.csv")

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# limpiar y normalizar
df["nombre"] = df["nombre"].str.strip().str.title()

# contar "Juan"
cantidad_juan = (df["nombre"] == "Juan").sum()

print("Cantidad de personas llamadas Juan:", cantidad_juan)