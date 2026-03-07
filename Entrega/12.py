import pandas as pd

# cargar dataset
df = pd.read_csv("data/personas.csv")

# detectar emails con espacios al inicio o final
emails_con_espacios = df["email"].astype(str).str.match(r'^\s+|\s+$')

# contar registros
cantidad_emails_con_espacios = emails_con_espacios.sum()

print("Registros con email que tiene espacios adicionales:", cantidad_emails_con_espacios)