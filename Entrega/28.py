import pandas as pd
import re

# Cargar dataset
df = pd.read_csv("data/personas.csv")

# Limpiar profesion 
def limpiar_profesion(texto):
    if pd.isna(texto):
        return texto
    texto = str(texto).strip()
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)
    return texto.strip().lower()

df["profesion_limpia"] = df["profesion"].apply(limpiar_profesion)

correcciones_residuales = {
    "electricist": "electricista",
    "periodist":   "periodista",
    "economist":   "economista"
}
df["profesion_limpia"] = df["profesion_limpia"].replace(correcciones_residuales)

# Limpiar salario
df["salario_str"] = df["salario"].astype(str)

reemplazos_salario = {
    "l": "1",
    "O": "0",
    "e": "3",
    "aprox.": ""
}

for old, new in reemplazos_salario.items():
    df["salario_str"] = df["salario_str"].str.replace(old, new, regex=False)

df["salario_str"] = df["salario_str"].str.replace(r',', '.', regex=True)
df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)
df["salario_limpio"] = pd.to_numeric(df["salario_limpio"], errors='coerce')

# Respuesta
promedio_por_profesion = df.groupby("profesion_limpia")["salario_limpio"].mean()
profesion_top = promedio_por_profesion.idxmax()
salario_top = promedio_por_profesion.max()

print(f"¿Cuál es la profesión con el salario promedio más alto?:{profesion_top.title()} con un promedio de ${salario_top:,.0f}")
