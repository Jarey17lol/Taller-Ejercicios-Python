import pandas as pd
import codecs
datos= pd.read_csv("data/personas.csv")

texto_original="chonga dayana"

texto_cifrado= codecs.encode(texto_original,'rot_13')
print(f"cifrado:{texto_cifrado}")

condicion=datos['nombre_cifrado']=='pubatn qnlnan'
datos_nuevos=datos[condicion]
print(datos)