
import os
import pandas as pd
try:
    data_df = pd.read_json(os.getcwd()+"/daten/autos.json", orient='records')
except Exception as e:
    print(e)
print("data_df", data_df)
print("*" * 50)
print("Zeilen", data_df.index)
print("*" * 50)
print("Spalten", data_df.columns)
print("*" * 50)
print("Typ", type(data_df))
print("*" * 50)
print("Dimension",data_df.ndim)
print("*" * 50)
print("Dimension als Tupel",data_df.shape)
print("*" * 50)
print("dtypes",data_df.dtypes)
print("*" * 50)
print("Werte",data_df.values)
print("*" * 50)
print("Achsen",data_df.axes)
print("*" * 50)
print("Anzahl der Elemente",data_df.size)
print("*" * 50)

export = data_df.to_json(os.getcwd()+"/daten/auto2.json", orient='records')
