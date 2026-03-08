# Taller de Python - Manejo y Limpieza de Datos

Taller de Limpieza y Análisis de Datos — personas.csv

Descripción del Dataset

El proyecto consiste en el análisis y limpieza de un conjunto de datos contenido en el archivo data/personas.csv. El dataset contiene información de personas y fue diseñado intencionalmente con errores y datos corruptos para practicar técnicas de limpieza y procesamiento de datos utilizando Python.

Características del dataset:

Archivo: data/personas.csv
Número de registros: aproximadamente 300,000 filas
Columnas:

* id
* nombre_cifrado
* apellido_cifrado
* ciudad
* profesion
* email
* fecha_nacimiento
* salario
* activo

Aproximadamente el 30% de los datos en cada columna contiene errores intencionales, como caracteres especiales, letras sustituidas por símbolos, formatos inconsistentes o texto adicional. Debido a esto, fue necesario realizar un proceso de limpieza antes de poder realizar consultas y análisis confiables.

Tecnologías Utilizadas

El proyecto se desarrolló utilizando las siguientes herramientas:

* Python 3
* Pandas para manipulación y análisis de datos
* Expresiones regulares (regex) para limpieza de texto
* Funciones personalizadas para normalización de datos

Carga del Dataset

El primer paso consistió en cargar el archivo CSV en un DataFrame de Pandas para poder manipular los datos de manera estructurada.

```python
import pandas as pd

df = pd.read_csv("data/personas.csv")
```

Limpieza de nombre_cifrado y apellido_cifrado

Los nombres y apellidos del dataset se encuentran cifrados usando el algoritmo ROT13. Antes de descifrarlos, se eliminan caracteres especiales que fueron insertados como ruido en los datos.

Los caracteres eliminados incluyen:

@ % # ! * _ ( ) [ ]

Luego de limpiar el texto, se aplica ROT13 para recuperar el nombre original y se normaliza el formato.

```python
import codecs
import re

def limpiar_y_descifrar(texto):
    texto = re.sub(r'[@%#()\[\]!_*]', '', str(texto))
    texto = texto.strip()
    texto = codecs.decode(texto, 'rot_13')
    return texto.strip().title()
```

Este proceso permite obtener nombres y apellidos correctamente formateados.

Limpieza de la columna ciudad

La columna ciudad presenta múltiples errores, principalmente sustituciones de letras por símbolos y caracteres decorativos. Por ejemplo:

C@li → Cali
Bogot@ → Bogota
M3d3llin → Medellin

Para solucionar esto se utilizó un diccionario de correcciones explícitas para los casos conocidos y posteriormente se eliminaron los caracteres especiales restantes.

```python
correcciones_ciudades = {
    "B@rr@nquill@": "Barranquilla",
    "Bogot@": "Bogota",
    "C@li": "Cali",
    "M3d3llin": "Medellin"
}

df["ciudad"] = df["ciudad"].str.strip()
df["ciudad"] = df["ciudad"].replace(correcciones_ciudades)
df["ciudad"] = df["ciudad"].str.replace(r'[@%#()\[\]!_*]', '', regex=True)
df["ciudad"] = df["ciudad"].str.strip().str.title()
```

Después de este proceso todas las ciudades quedan con formato consistente y sin caracteres corruptos.

Limpieza de la columna profesion

La columna profesión fue una de las más complejas debido a la variedad de errores presentes. Se identificaron tres tipos principales de problemas:

1. Caracteres decorativos al inicio o final del texto
   Ejemplos:
   @CONTADOR@
   ***Traductor
   #Quimico

2. Sustituciones de letras por símbolos dentro de la palabra
   Ejemplos:
   Ing3ni3ro
   Cont@dor
   M3c@nico

3. Palabras incompletas o truncadas
   Ejemplos:
   Periodist
   Electricist
   Economist

Para resolver estos problemas se utilizó una función que reemplaza símbolos solo cuando están entre letras y elimina caracteres decorativos restantes.

```python
def limpiar_profesion(texto):
    texto = str(texto).strip()
    texto = re.sub(r'(?<=[a-zA-Z])3(?=[a-zA-Z])', 'e', texto)
    texto = re.sub(r'(?<=[a-zA-Z])@(?=[a-zA-Z])', 'a', texto)
    texto = re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ\s]', '', texto)
    return texto.strip().lower()
```

También se aplicaron correcciones residuales para palabras que quedaron incompletas.

```python
correcciones_residuales = {
    "electricist": "electricista",
    "periodist": "periodista",
    "economist": "economista"
}
```

Después de aplicar todas las transformaciones, el dataset quedó con aproximadamente 25 profesiones únicas correctamente normalizadas.

Limpieza de la columna salario

La columna salario presenta errores donde algunas letras sustituyen números y aparece texto adicional como “aprox.”.

Para corregirlo se realizaron reemplazos y posteriormente se eliminaron todos los caracteres que no fueran números o punto decimal.

```python
reemplazos_salario = {
    "l": "1",
    "O": "0",
    "e": "3",
    "aprox.": ""
}

df["salario_limpio"] = df["salario_str"].str.replace(r'[^0-9.]', '', regex=True)
df["salario_limpio"] = pd.to_numeric(df["salario_limpio"], errors='coerce')
```

De esta forma el salario queda almacenado como valor numérico que puede utilizarse para cálculos o análisis estadísticos.

Limpieza de la columna fecha_nacimiento

Las fechas presentan múltiples formatos diferentes, como:

yyyy/mm/dd
dd-mm-yyyy
yyyy.mm.dd

Además pueden contener caracteres adicionales. Para normalizar todas las fechas se creó una función que limpia el texto y convierte el formato al estándar yyyy-mm-dd.

```python
def limpiar_fecha(fecha):
    fecha = re.sub(r'[^0-9\-/. ]', '', str(fecha))
    fecha = re.sub(r'[ /.]', '-', fecha)
    match = re.match(r'(\d{4})-(\d{1,2})-(\d{1,2})', fecha)
    if match:
        y, m, d = match.groups()
        return f"{y}-{int(m):02d}-{int(d):02d}"
    return fecha
```

Esto permite tener un formato uniforme en todas las fechas del dataset.

Limpieza de la columna activo

La columna activo contiene múltiples representaciones de valores booleanos, como:

true
false
1
0
si
sí
yes
no

Todos estos valores se transformaron a un formato booleano estándar.

```python
df["activo_bool"] = df["activo_str"].map({
    "true": True, "1": True, "si": True, "sí": True, "yes": True,
    "false": False, "0": False, "no": False, "n": False
}).fillna(False)
```

De esta manera la columna puede utilizarse fácilmente para filtros y análisis.

Limpieza de la columna email

Los correos electrónicos presentan varios tipos de errores comunes:

* Uso de mayúsculas en dominios
* Paréntesis o corchetes alrededor del email
* Espacios alrededor del símbolo @
* Espacios en los puntos del dominio
* Prefijo "mailto:"
* Dominio incorrecto como mail.com en lugar de gmail.com

Para corregir estos problemas se implementó la siguiente función:

```python
def limpiar_email(texto):
    texto = texto.lower()
    texto = re.sub(r'^mailto:', '', texto)
    texto = re.sub(r'[()<>]', '', texto)
    texto = re.sub(r'\s*@\s*', '@', texto)
    texto = re.sub(r'\s*\.\s*', '.', texto)
    texto = re.sub(r'@mail\.com$', '@gmail.com', texto)
    return texto.strip()
```

Esto permite obtener direcciones de correo limpias y consistentes.

Consultas y Análisis de Datos

Una vez completado el proceso de limpieza del dataset, se realizaron diversas consultas para responder preguntas específicas del taller. Estas consultas se basan en filtros aplicados sobre el DataFrame utilizando Pandas.

Por ejemplo, para determinar cuántos registros tienen nombre "Carlos" y viven en la ciudad de "Cali" se utilizó un filtro combinado:

```python
df[(df["nombre"] == "Carlos") & (df["ciudad"] == "Cali")]
```

Para obtener únicamente el número de registros se utilizó:

```python
cantidad = df[(df["nombre"] == "Carlos") & (df["ciudad"] == "Cali")].shape[0]
```

Conclusión

Este proyecto permitió aplicar diferentes técnicas de limpieza y transformación de datos utilizando Python. Se trabajó con múltiples tipos de errores comunes en datasets reales, como caracteres especiales, sustitución de letras por símbolos, formatos inconsistentes y datos incompletos.

Mediante el uso de Pandas, expresiones regulares y funciones personalizadas se logró transformar un dataset altamente corrupto en un conjunto de datos limpio y consistente, listo para análisis posteriores.

