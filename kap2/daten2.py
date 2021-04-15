from openpyxl import Workbook
from openpyxl import load_workbook
try:
    wb = load_workbook("daten/datei3.xlsx")
    ws=wb.active
except:
    print("Fehler beim Einlesen der Datei")
for row in ws.values:
    print(row)
for row in ws.values:
       for value in row:
            print(value)
