
import os
import json
try:
    with open(os.getcwd()+"/daten/autos.json") as f:
        daten = json.load(f)
    print(daten, type(daten))
    for row in daten:
        print(row)
        print(row['name'])
    
except Exception as e:
    print(e)
