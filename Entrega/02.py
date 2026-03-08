import pandas as pd
import codecs

# cargar dataset
df = pd.read_csv("data/personas.csv")

# descifrar nombres
df["nombre"] = df["nombre_cifrado"].apply(lambda x: codecs.decode(str(x), 'rot_13'))

# contar cuantas veces aparece Maria
cantidad_maria = (df["nombre"].str.strip().str.title() == "Maria").sum()

print("Cantidad de personas llamadas Maria:", cantidad_maria)