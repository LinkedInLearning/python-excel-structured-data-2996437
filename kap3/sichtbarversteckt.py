from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.chart import PieChart, BarChart, Reference, Series

try:
    wb = load_workbook("daten/datei1.xlsx")
    ws = wb.active
except:
    print("Fehler beim Einlesen der Datei")
ws.column_dimensions['B','D'].hidden=True
#ws.row_dimensions[[5,9,14]].hidden=True


try:
    wb.save("daten/dateiausgeblendet.xlsx")
  
except Exception:
    print("Fehler beim Schreiben der Exceldatei")
