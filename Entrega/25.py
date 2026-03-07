import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# Función para limpiar profesiones (manteniendo coherencia con limpieza previa)
def limpiar_texto(texto):
    texto = str(texto).strip()
    texto = re.sub(r'[^a-zA-Záéíóúñ ]', '', texto)  # eliminar caracteres especiales
    return texto.lower()

df["profesion"] = df["profesion"].apply(limpiar_texto)

# Función para limpiar salarios de manera robusta
def limpiar_salario(sal):
    if pd.isna(sal):
        return 0
    sal = str(sal).lower().strip()
    # eliminar todos los caracteres no numéricos y palabras como 'aprox'
    sal = re.sub(r'[^0-9]', '', sal)
    return int(sal) if sal.isdigit() else 0

df["salario_limpio"] = df["salario"].apply(limpiar_salario)

# Filtrar registros con profesión "abogado" y salario > 10,000,000
mask = (df["profesion"] == "abogado") & (df["salario_limpio"] > 10000000)

# Contar registros
cantidad_abogado_altosalario = mask.sum()

# Mostrar resultado
print(f"Cantidad de registros con profesión 'Abogado' y salario > 10,000,000: {cantidad_abogado_altosalario}")