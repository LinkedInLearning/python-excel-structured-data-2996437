# Einlesen einer Excel-Datei und Zerlegen der Daten in verwertbare Einzelinformationen mit Pandas - 
# xlrd muss installiert sein (pip install xlrd)
import os
import pandas as pd
daten=pd.read_excel(os.getcwd()+"/daten/Messwerte.xlsx",sheet_name='Upload', index_col=None, header=0) 


print("Daten\n", daten.loc[0])
print("*" * 50)
print("Daten\n", daten.loc[0:0])
print("*" * 50)
