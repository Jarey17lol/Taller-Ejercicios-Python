import pandas as pd

datos= pd.read_csv("data/personas.csv")
print (datos.sample(100))

