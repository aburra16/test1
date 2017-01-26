import csv
import numpy as np
import scipy
import pandas

fl = open("claimtest1.csv", "r")
csvfl = csv.reader(fl, delimiter = ",")

Date = []
Amount = []
Payer = []

ClaimList = []

PayerList = []

next(csvfl)
# for row in csvfl:
#     f1 = row[0]
#     f2 = row[1]
#     f3 = row[2]
#     Date.append(f1)
#     Amount.append(float(f3))
#     Payer.append(f2)
#
# print(*Amount, sep="\n")
# print("Mean :", np.mean(Amount))

class Family:

    def __init__(self, name, count, amount):
        self.name = name
        self.count = count
        self.amount = amount

class Claim:

    clmCount = 0

    def __init__(self, clmDate, clmPayer, clmAmount):
        self.clmDate = clmDate
        self.clmPayer = clmPayer
        self.clmAmount = clmAmount
        Claim.clmCount +=1

#Populate claim list from CSV
for row in csvfl:
    PayerList.append(row[1])
    ClaimList.append(Claim(row[0],row[1], float(row[2])))

UniquePayers = list(set(PayerList))

Aetna = []
Medicare = []
Empire = []
FamilyList = []

#Create blank FamilyList with Payer Name
for i in range(len(UniquePayers)):
    iFam = Family(UniquePayers[i],0,0)
    FamilyList.append(iFam)

for cl in ClaimList:
    for i in range(len(FamilyList)):
        if cl.clmPayer == FamilyList[i].name:
            FamilyList[i].amount += cl.clmAmount
            FamilyList[i].count += 1


outputFile = open("OutputCSV.csv", "w")
csvWR = csv.writer(outputFile)
CSVheader = ["Insurance", "Count", "Amount", "Average"]
csvWR.writerow(CSVheader)

DataOut = []

for i in range(len(FamilyList)):
    print(FamilyList[i].name, ": ", "Count = ", FamilyList[i].count, "; Amount = ", FamilyList[i].amount, sep='')
    average = float(FamilyList[i].amount) / float(FamilyList[i].count)
    csvWR.writerow([FamilyList[i].name, FamilyList[i].count, FamilyList[i].amount, average])

fl.close()