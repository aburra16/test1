import csv
import numpy as np
import scipy
import pandas as pd

#Read in file to build allowable amounts matrix
fl1 = open("AllowableAmts.csv", "r")
csvfl1 = csv.reader(fl1, delimiter = ",")

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

    def __init__(self, clmDate, clmHosp, clmPayer, clmProcedure, clmAmount):
        self.clmDate = clmDate
        self.clmHosp = clmHosp
        self.clmPayer = clmPayer
        self.clmProcedure = clmProcedure
        self.clmAmount = clmAmount
        Claim.clmCount +=1

class PayerAllowable:

    def __init__(self, name, procedure, allowable):
        self.name = name
        self.procedure = procedure
        self.allowable = allowable


#Populate allowable amounts list from CSV
PayerList = next(csvfl1)
for row in csvfl1:
    for i in range(1,len(PayerList)):
        AllowableList.append(PayerAllowable(PayerList[i],row[0],float(row[i])))


fl1.close()

#read in file to build claims list
fl2 = open("Claims.csv", "r")
csvfl2 = csv.reader(fl2, delimiter = ",")


#Populate with claims and blank billed amount
next(csvfl2) #skip header
for row in csvfl2:
    ClaimList.append(Claim(row[0],row[1],row[2],row[3],0))

#Update claim billed amount from allowable list
for j in range(len(ClaimList)):
    for i in range(len(AllowableList)):
        if (AllowableList[i].name == ClaimList[j].clmPayer and
                    AllowableList[i].procedure == ClaimList[j].clmProcedure):
            ClaimList[j].clmAmount = np.random.normal(AllowableList[i].allowable, 0.1*AllowableList[i].allowable)
        else:
            pass
print("Claim list populated", sep='')


fl2.close()


# for i in range(len(ClaimList)):
#     print(ClaimList[i].clmdate, ": " , ClaimList[i].clmHosp, "  ", ClaimList[i].clmPayer,"  ", ClaimList[i].clmProcedure,"  ", ClaimList[i].clmAmount,sep='')


outputFile = open("OutputCSV.csv", "w")
csvWR = csv.writer(outputFile)
CSVheader = ["Claim Date", "Facility", "Payer", "Procedure", "Billed Amount"]
csvWR.writerow(CSVheader)

for i in range(len(ClaimList)):
    csvWR.writerow([ClaimList[i].clmDate, ClaimList[i].clmHosp, ClaimList[i].clmPayer, ClaimList[i].clmProcedure, ClaimList[i].clmAmount])
    print("Writing row : ", i, sep='')
outputFile.close()