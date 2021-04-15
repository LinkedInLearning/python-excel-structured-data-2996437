from openpyxl import Workbook
from openpyxl import load_workbook

try:
    wb = load_workbook("daten/datei3.xlsx")
    ws=wb.active
except:
    print("Fehler beim Einlesen der Datei")
#ws.delete_cols(3, 3)
#ws.delete_rows(6, 3)
#ws.insert_rows(7)
#ws.insert_rows(7,5)
#ws.insert_cols(3)
ws.move_range("D4:F10", rows=-2, cols=5)
try:
    wb.save("daten/datei6.xlsx")
except:
    print("Fehler beim Schreiben der Exceldatei")