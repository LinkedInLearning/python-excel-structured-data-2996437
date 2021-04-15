from openpyxl import Workbook
from openpyxl import load_workbook
try:
    wb = load_workbook("daten/datei3.xlsx")
except:
    print("Fehler beim Einlesen der Datei")
ws = wb.active
# Zu druckender Bereich
ws.print_area = 'A1:D5'
# Ausrichtung auf dem Blatt
ws.print_options.horizontalCentered = True
ws.print_options.verticalCentered = True
# Titel
ws.oddHeader.left.text = "Seite &[Page] von &N"
ws.oddHeader.left.size = 14
ws.oddHeader.left.font = "Tahoma,Bold"
ws.oddHeader.left.color = "CC3366"
# Titelangaben für Spalten und Zeilen
ws.print_title_cols = 'A:B' # Die ersten zwei Spalten
ws.print_title_rows = '1:1' # Erste Reihe

try:
    wb.save("daten/datei3.xlsx")
except:
    print("Fehler beim Schreiben der Exceldatei")