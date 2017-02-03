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
FamilyList = []

#Arrays for randomization of payment time and haircut
avgTime = [27,29,14,23,12,16,25]
stdTime = [0.1,0.14,0.12,0.04,0.13,0.07,0.16]
avgHaircut = [0.12,0.35,0.42,0.27,0.19,0.44,0.28]
stdHaircut = [0.11,0.16,0.05,0.19,0.22,0.38,0.08]

class Family:

    def __init__(self, name, count, avgTime, stdTime, haircut, stdHaircut):
        self.name = name
        self.count = count
        self.avgTime = avgTime
        self.stdTime = stdTime
        self.haircut = haircut
        self.stdHaircut = stdHaircut

class Claim:

    clmCount = 0

    def __init__(self, clmDate, clmHosp, clmPayer, clmProcedure, clmAmount,remitAmount, remitTime):
        self.clmDate = clmDate
        self.clmHosp = clmHosp
        self.clmPayer = clmPayer
        self.clmProcedure = clmProcedure
        self.clmAmount = clmAmount
        self.remitAmount = remitAmount
        self.remitTime = remitTime
        Claim.clmCount +=1

class PayerAllowable:

    def __init__(self, name, procedure, allowable):
        self.name = name
        self.procedure = procedure
        self.allowable = allowable


#Populate allowable amounts list from CSV
PayerList = next(csvfl1)
PayerList.pop(0)

    #first set up families
for i in range(len(PayerList)):
    FamilyList.append(Family(PayerList[i],0,avgTime[i], stdTime[i], avgHaircut[i], stdHaircut[i]))

for row in csvfl1:
    for i in range(len(PayerList)):
        AllowableList.append(PayerAllowable(PayerList[i],row[0],float(row[i+1])))


fl1.close()

#read in file to build claims list
fl2 = open("Claims.csv", "r")
csvfl2 = csv.reader(fl2, delimiter = ",")


#Populate with claims and blanks for amounts and times
next(csvfl2) #skip header
for row in csvfl2:
    ClaimList.append(Claim(row[0],row[1],row[2],row[3],0,0,0))

#Update claim billed amount from allowable list
for j in range(len(ClaimList)):
    for i in range(len(AllowableList)):
        if (AllowableList[i].name == ClaimList[j].clmPayer and
                    AllowableList[i].procedure == ClaimList[j].clmProcedure):
            ClaimList[j].clmAmount = np.random.normal(AllowableList[i].allowable, 0.1*AllowableList[i].allowable)
            #Now insert remit amounts and times
            for k in range(len(PayerList)):
                if FamilyList[k].name == ClaimList[j].clmPayer:
                    ClaimList[j].remitAmount = ClaimList[j].clmAmount*(1- np.random.normal(FamilyList[k].haircut, FamilyList[k].haircut*FamilyList[k].stdHaircut))
                    ClaimList[j].remitTime = np.random.normal(FamilyList[k].avgTime, FamilyList[k].stdTime*FamilyList[k].avgTime)
                    FamilyList[k].count +=1
                else:
                    pass
        else:
            pass
print("Claim list populated", sep='')


fl2.close()


# for i in range(len(ClaimList)):
#     print(ClaimList[i].clmdate, ": " , ClaimList[i].clmHosp, "  ", ClaimList[i].clmPayer,"  ", ClaimList[i].clmProcedure,"  ", ClaimList[i].clmAmount,sep='')


outputFile = open("OutputCSV.csv", "w")
csvWR = csv.writer(outputFile)
CSVheader = ["Claim Date", "Facility", "Payer", "Procedure", "Billed Amount", "Remit Amount", "Remit Days"]
csvWR.writerow(CSVheader)

for i in range(len(ClaimList)):
    csvWR.writerow([ClaimList[i].clmDate, ClaimList[i].clmHosp, ClaimList[i].clmPayer, ClaimList[i].clmProcedure, ClaimList[i].clmAmount, ClaimList[i].remitAmount, ClaimList[i].remitTime])
    print("Writing row : ", i, sep='')
outputFile.close()