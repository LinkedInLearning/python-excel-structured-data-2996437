# Einlesen einer gewissen Anzahl an Zeichen aus einer Textdatei
import os
fp=open(os.getcwd()+"\\daten\\dummytext2.txt","r")
print(fp.read(12))
fp.close()
