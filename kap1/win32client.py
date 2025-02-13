import win32com.client
import os

excel = win32com.client.Dispatch("Excel.Application")  # Excel starten
wb = excel.Workbooks.Open(os.getcwd()+"\\datei.xlsx")  # Datei öffnen
sheet = wb.Sheets("Tabelle1")  # Blatt auswählen

wert = sheet.Cells(1, 1).Value  # Zelle A1 auslesen
print(wert)

wb.Close(SaveChanges=0)  # Datei schließen
excel.Quit()  # Excel beenden

