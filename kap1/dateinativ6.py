# Einlesen einer strukturierten Textdatei und Zerlegen der Daten in verwertbare Einzelinformationen
import os
daten=[]
fp=open(os.getcwd()+"/daten/autos.csv","r")
for line in fp:
    daten.append(line.split(","))
fp.close()
print(daten)
print("*" * 50)
print(daten[2:5])
print("*" * 50)
print(daten[2][0])