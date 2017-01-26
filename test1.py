import csv
import numpy as np
import scipy
import pandas

fl = open("claimtest1.csv", "r")
csvfl = csv.reader(fl, delimiter = ",")

ClaimList = []

PayerList = []


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
next(csvfl)
for row in csvfl:
    PayerList.append(row[1])
    ClaimList.append(Claim(row[0],row[1], float(row[2])))

UniquePayers = list(set(PayerList))

FamilyList = []

#Create blank FamilyList with Payer Name
for i in range(len(UniquePayers)):
    iFam = Family(UniquePayers[i],0,0)
    FamilyList.append(iFam)

#Populate Family list with amounts
for cl in ClaimList:
    for i in range(len(FamilyList)):
        if cl.clmPayer == FamilyList[i].name:
            FamilyList[i].amount += cl.clmAmount
            FamilyList[i].count += 1


outputFile = open("OutputCSV.csv", "w")
csvWR = csv.writer(outputFile)
CSVheader = ["Insurance", "Count", "Amount", "Average"]
csvWR.writerow(CSVheader)

for i in range(len(FamilyList)):
    print(FamilyList[i].name, ": ", "Count = ", FamilyList[i].count, "; Amount = ", FamilyList[i].amount, sep='')
    average = FamilyList[i].amount / FamilyList[i].count
    csvWR.writerow([FamilyList[i].name, FamilyList[i].count, FamilyList[i].amount, average])

fl.close()
outputFile.close()