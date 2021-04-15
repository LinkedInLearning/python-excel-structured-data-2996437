# Einfaches, zeilenweises Einlesen einer Textdatei
import os
fp=open(os.getcwd()+"\\daten\\dummytext1.txt","r")
for line in fp:
    print(line.rstrip())
fp.close()

