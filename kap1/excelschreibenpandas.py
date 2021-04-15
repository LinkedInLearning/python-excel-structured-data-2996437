# Schreiben CSV-Datei mit Pandas
# Implizit wird openpyxl verwendet!!
import os
import pandas as pd
daten=pd.read_csv(os.getcwd()+"/daten/autos.csv")
cols = [0,2,3,4]
df1 = daten[daten.columns[cols]]
cols = [0,5,7,8]
df2 = daten[daten.columns[cols]]

with pd.ExcelWriter(os.getcwd()+"/daten/autoextrakt.xlsx") as writer:

    df1.to_excel(writer, sheet_name='Sheet1')

    df2.to_excel(writer, sheet_name='Sheet2')