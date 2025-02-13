import os
from pyxlsb import open_workbook

with open_workbook("datei.xlsb") as wb:
    with wb.get_sheet(1) as sheet:  # Erstes Tabellenblatt
        for row in sheet.rows():
            print([item.v for item in row])
