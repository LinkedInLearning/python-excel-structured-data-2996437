
import os
import csv
try:
    with open(os.getcwd()+"/daten/autos.csv", newline='') as csvfile:
        myreader = csv.reader(csvfile)
        print(myreader, type(myreader))
        for row in myreader:
            print(row, type(row))
            print(', '.join(row))
except Exception as e:
    print(e)
