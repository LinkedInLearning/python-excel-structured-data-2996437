from openpyxl import Workbook
from openpyxl import load_workbook
try:
    wb = load_workbook("daten/pivot.xlsx")
except:
    print("Fehler beim Einlesen der Datei")

ws=wb.active

for x in ws._pivots:
    print(x)
    print("*" * 50)
pivot = ws._pivots[0] 
print(pivot.name)

for x in pivot.rowItems:
    print(x.t)
   
pivot.cache.refreshOnLoad = True