# Einfaches SChreiben einer Textdatei
import os
fp=open(os.getcwd()+"\\daten\\zitat.txt","w")
fp.write("Lovely spam, wonderful spa-a-m, Lovely spam, wonderful Spam")
fp.close()
