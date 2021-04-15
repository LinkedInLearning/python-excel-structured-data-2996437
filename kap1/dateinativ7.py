# Komplette Absicherung mit Ausnahmebehandlung
import os
try:
    fp=open(os.getcwd()+"/daten/zitat.txt","r")
    print(fp.read())
    fp.close()
   
except ValueError:
    print("Fehler 1")
except FileNotFoundError as e:
    print("Fehler 2", e)
    raise e
except Exception as e:
    print(e)
except:
    print("Lumpensammler")
else:
    print("Alles gut",fp)
    
finally:
    print("Das machen wir immer")
print("Nach der Leseaktion")
