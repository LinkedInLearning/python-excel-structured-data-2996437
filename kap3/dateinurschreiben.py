from openpyxl import Workbook
wb = Workbook(write_only=True)
ws = wb.create_sheet()
for i in range(10):
    ws.append([1,2,3,4,5])

try:
    wb.save("daten/datei3.xlsx")
except:
    print("Fehler beim Schreiben der Exceldatei")
