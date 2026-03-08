import pandas as pd
import re

# cargar dataset
df = pd.read_csv("data/personas.csv")

# correcciones específicas encontradas
correcciones_ciudades = {
    "S@nt@ M@rt@": "Santa Marta",
    "V@ll3dup@r": "Valledupar",
    "M@niz@l3s": "Manizales",
    "Sinc3l3jo": "Sincelejo",
    "Buc@r@m@ng@": "Bucaramanga",
    "Tunj@": "Tunja",
    "Ib@gu3": "Ibague",
    "C@rt@g3n@": "Cartagena",
    "Arm3ni@": "Armenia",
    "M3d3llin": "Medellin",
    "Cucut@": "Cucuta",
    "C@li": "Cali",
    "P3r3ir@": "Pereira",
    "Mont3ri@": "Monteria",
    "Bogot@": "Bogota",
    "Vill@vic3ncio": "Villavicencio",
    "N3iv@": "Neiva",
    "Pop@y@n": "Popayan",
    "B@rr@nquill@": "Barranquilla",
    "P@sto": "Pasto"
}

# corregir ciudades
df["ciudad"] = df["ciudad"].replace(correcciones_ciudades)

# limpiar caracteres especiales
df["ciudad"] = df["ciudad"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)

# normalizar
df["ciudad"] = df["ciudad"].str.strip().str.title()

# ciudades unicas
ciudades_unicas = df["ciudad"].nunique()

print("Cantidad de ciudades unicas después de normalizar:", ciudades_unicas)