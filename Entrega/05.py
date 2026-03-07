import pandas as pd
import codecs

# cargar dataset
df = pd.read_csv("data/personas.csv")

# descifrar apellidos
df["apellido"] = df["apellido_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# limpiar datos
df["apellido"] = df["apellido"].str.strip().str.title()

# encontrar el apellido más frecuente
apellido_mas_frecuente = df["apellido"].value_counts().idxmax()
cantidad = df["apellido"].value_counts().max()

print("Apellido más frecuente:", apellido_mas_frecuente)
print("Cantidad de veces:", cantidad)