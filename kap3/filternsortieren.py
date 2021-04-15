from openpyxl import Workbook
from openpyxl import load_workbook
try:
    wb = load_workbook("daten/pivot.xlsx")
except:
    print("Fehler beim Einlesen der Datei")
print(wb._active_sheet_index)    
wb._active_sheet_index=1
ws = wb.active
for row in ws.values:
    print(row)
ws.auto_filter.ref = "A1:F26"
ws.auto_filter.add_filter_column(1, ["Beratung"])
ws.auto_filter.add_sort_condition("B2:B26")
try:
  wb.save("daten/datei3gefiltert.xlsx")
except:
    print("Fehler beim Schreiben der Exceldatei")