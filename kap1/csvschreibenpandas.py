# Schreiben CSV-Datei mit Pandas
import os
import pandas as pd
daten=pd.read_csv(os.getcwd()+"/daten/autos.csv")
print(daten)
print("*" * 50)
cols = [0,2,3,4]
print(cols)
print("*" * 50)
df = daten[daten.columns[cols]]
print(df)
df.to_csv(os.getcwd()+"/daten/autosextrakt3.csv", index=False)