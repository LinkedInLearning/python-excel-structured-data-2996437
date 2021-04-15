# Einfaches, vollständiges Einlesen einer Textdatei in einem anderen Verzeichnis
import os

fp=open(os.path.abspath(".")+"\\daten\\dummytext1.txt","r")
print(fp.read())
fp.close()
print("*" * 50)
fp=open(os.getcwd()+"\\daten\\dummytext2.txt","r")
print(fp.read())
fp.close()

print("*" * 50)
fp=open(os.getcwd()+"/daten/dummytext3.txt","r")
print(fp.read())
fp.close()

