import csv
import numpy as np
import scipy
import pandas

fl1 = open("AllowableAmts.csv", "r")
csvfl = csv.reader(fl1, delimiter = ",")

ClaimList = []
ProcedureList = []
PayerList = []
AllowableList = []


class Family:

    def __init__(self, name, count, amount):
        self.name = name
        self.count = count
        self.amount = amount

class Claim:

    clmCount = 0

    def __init__(self, clmHosp, clmPayer, clmAmount):
        self.clmHosp = clmHosp
        self.clmPayer = clmPayer
        self.clmAmount = clmAmount
        Claim.clmCount +=1

class PayerAllowable:

    def __init__(self, name, procedure, allowable):
        self.name = name
        self.procedure = procedure
        self.allowable = allowable


#Populate allowable amounts list from CSV
PayerList = next(csvfl)
for row in csvfl:
    AllowableList.append(PayerAllowable(PayerList[1],row[0],row[1]))
    AllowableList.append(PayerAllowable(PayerList[2], row[0], row[2]))
    AllowableList.append(PayerAllowable(PayerList[3], row[0], row[3]))
    AllowableList.append(PayerAllowable(PayerList[4], row[0], row[4]))
    AllowableList.append(PayerAllowable(PayerList[5], row[0], row[5]))
    AllowableList.append(PayerAllowable(PayerList[6], row[0], row[6]))
    AllowableList.append(PayerAllowable(PayerList[7], row[0], row[7]))

fl1.close()

#Generate Billed Amounts
numClaims = 89908


for i in range(len(AllowableList)):
    print(AllowableList[i].name, ": " , AllowableList[i].procedure, "  ", AllowableList[i].allowable,sep='')


#outputFile = open("OutputCSV.csv", "w")
#csvWR = csv.writer(outputFile)
#CSVheader = ["Insurance", "Count", "Amount", "Average"]
#csvWR.writerow(CSVheader)

# for i in range(len(FamilyList)):
#     print(FamilyList[i].name, ": ", "Count = ", FamilyList[i].count, "; Amount = ", FamilyList[i].amount, sep='')
#     average = FamilyList[i].amount / FamilyList[i].count
#     csvWR.writerow([FamilyList[i].name, FamilyList[i].count, FamilyList[i].amount, average])

#outputFile.close()