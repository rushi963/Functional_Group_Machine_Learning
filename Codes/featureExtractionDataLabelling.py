'''
    Code feature extraction and data labeling from csv files containing FT-IR spectrum data
    Features: 1. transmission level for each bond type
                2. Percentage of points below threshold showing the existence of bond in the given bond range
'''

import csv
from os import listdir, path
from os.path import isfile, join
from pandas import DataFrame
import os

dataPath = "csvData_300_3FGs/"

bondRanges = {"1_1": (2850, 2950), "1_2": (3000, 3100), "1_3": (3290, 3310), "1_4": (3000, 3040), 
                    "2_1": (1620, 1680), "2_2": (1400, 1620), 
                    "3_1": (2100, 2260), 
                    "4_1": (1690, 1740), "4_2": (1710, 1780), "4_3": (1630, 1690), "4_4": (1680, 1750), "4_5": (1735, 1750), 
                    "5_1": (3300, 3500), "5_2": (3100, 3500), 
                    "6_1": (2500, 3200), "6_2": (3200, 3700), 
                    "7_1": (2220, 2260), 
                    "8_1": (1025, 1220), "8_2": (1250, 1360), 
                    "9_1": (1040, 1210), "9_2": (1210, 1320)}

# name of the functional group as stored in the name of the csv file
functionalGroups = {"carboxylicAcid": [], "amide": [], "aldehyde": []}

bondsPresentAbsent = {}
transmittance = {}
percentPts = {}
for key in sorted(bondRanges):
    transmittance[key] = []
    percentPts[key] = []
    bondsPresentAbsent[key] = []

transmittanceThreshold = 85

# Lists to store sample SDBS No and functional group
sample = []

# reading from csv file
for csvFileName in listdir(dataPath):
    fl = csvFileName.split(".")

    with open(os.path.join(dataPath, csvFileName),'rt') as csvfile:
        dictreader = csv.DictReader(csvfile)

        transLevelLst = {}
        for key in sorted(bondRanges):
            transLevelLst[key] = [100]

        totalPts = {}

        dataPts = []

        for row in dictreader:

            dataPts.append( ( float(row['Wave Number (cm-1)']), float(row['Transmittance (%T)']) ) )

            for key in sorted(bondRanges):
                if dataPts[-1][0] >= bondRanges[key][0] and dataPts[-1][0] <= bondRanges[key][1]:
                    totalPts[key] = totalPts.get(key, 0) + 1
                    if dataPts[-1][1] <= transmittanceThreshold:
                        transLevelLst[key].append(dataPts[-1][1])


    for key in sorted(bondRanges):
        transmittance[key].append(min(transLevelLst[key]))
        percentPts[key].append( (len(transLevelLst[key]) - 1) / float(totalPts[key]) * 100 )
        if transmittance[key][-1] < 100:
            bondsPresentAbsent[key].append(1)
        else:
            bondsPresentAbsent[key].append(0)

    # finding out the functional group from sample name and storing it as 1 if present
    filename = fl[0].split("_")
    name = filename[1]

    for key in functionalGroups.keys():
        if name == key:
            functionalGroups[key].append(1)
        else:
            functionalGroups[key].append(0)

# store sample SDBS No and functional group
    sample.append(filename[0])


# csv file with transmittance levels and percentage points
dfDict = {'Sample': sample}
for key in sorted(bondRanges):
    dfDict[str('Transmittance' + key)] = transmittance[key]
    dfDict[str('PercentPointsBelowThreshold' + key)] = percentPts[key]

for key in functionalGroups.keys():
    dfDict[key] = functionalGroups[key]

df = DataFrame(dfDict)

dfCols = ['Sample']
for key in sorted(bondRanges):
    dfCols.append(str('Transmittance' + key))
    dfCols.append(str('PercentPointsBelowThreshold' + key))

for key in functionalGroups.keys():
    dfCols.append(key)

df = df[dfCols]

Data = "LabelledData/"

if not os.path.exists(Data):
    os.makedirs(Data)

df.to_csv(Data + "ML_Data_modifiedFeatures_300" + ".csv", sep=',', encoding='utf-8', index=False)

print("csv file with transmittance levels and percentage points generated.")

# csv file with only transmittance levels
dfCols = ['Sample']
for key in sorted(bondRanges):
    dfCols.append(str('Transmittance' + key))

for key in functionalGroups.keys():
    dfCols.append(key)

df = df[dfCols]

df.to_csv(Data + "ML_Data_only_transmittance_300" + ".csv", sep=',', encoding='utf-8', index=False)

print("csv file with only transmittance levels generated.")