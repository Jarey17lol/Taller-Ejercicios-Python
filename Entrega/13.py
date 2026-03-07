import pandas as pd

# cargar dataset
df = pd.read_csv("data/personas.csv")

# detectar salarios con caracteres no numéricos
salarios_no_numericos = ~df["salario"].astype(str).str.match(r'^\d+$')

# contar registros
cantidad_salarios_no_numericos = salarios_no_numericos.sum()

print("Registros con salario que contiene caracteres no numéricos:", cantidad_salarios_no_numericos)