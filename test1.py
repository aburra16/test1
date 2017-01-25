import csv
import numpy as np
import scipy
import pandas

fl = open("claimtest1.csv", "r")
csvfl = csv.reader(fl, delimiter = ",")

Date = []
Amount = []
Payer = []

next(csvfl)
for row in csvfl:
    f1 = row[0]
    f2 = row[1]
    f3 = row[2]
    Date.append(f1)
    Amount.append(float(f3))
    Payer.append(f2)

#for i in Amount:
    #float(i)

print(*Amount, sep="\n")
print("Mean :", np.mean(Amount))
