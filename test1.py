import csv
import numpy
import scipy
import pandas

fl = open("claimtest1.csv", "rt")
csvfl = csv.reader(fl, delimiter = ",")

Date = []
Amount = []
Payer = []

header = next(csvfl)
for row in csvfl:
    f1 = row[0]
    f2 = row[1]
    f3 = row[2]
    Date.append(f1)
    Amount.append(float(f3))
    Payer.append(f2)

print(Amount, sep = "\n")
#print(numpy.mean(Amount), sep="\n")
