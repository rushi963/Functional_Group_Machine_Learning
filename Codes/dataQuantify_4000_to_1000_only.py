'''
    Code feature extraction and data labeling from csv files containing FT-IR spectrum data
    Features: 1. transmission level for each bond type
'''

dataPath = "csvData_700_7FGs/"

import csv
from os import listdir, path
from os.path import isfile, join
from pandas import DataFrame
import os


for csvFileName in listdir(dataPath):
    fl = csvFileName.split(".")

    with open(os.path.join(dataPath, csvFileName),'rt') as csvfile:
        dictreader = csv.DictReader(csvfile)

        waveNumber = []
        transmittance = []
        for row in dictreader:
            waveNumber.append((float(row['Wave Number (cm-1)'])))
            transmittance.append((float(row['Transmittance (%T)'])))

            if waveNumber[-1] < 1000.0:
                break

                # Convert the wave nos and transmittance to a DataFrame i.e. a table
        df = DataFrame({'Wave Number (cm-1)': waveNumber, 'Transmittance (%T)': transmittance})

        # adjust the columns of DataFrame
        dfCols = ['Wave Number (cm-1)', 'Transmittance (%T)']
        df = df[dfCols]

        # Directory Where csv data files are stored
        destinationPath = "csvData_700_7FGs_4000_to_1000/"

        # check if a directory exists to store csv files
        if not os.path.exists(destinationPath):
            os.makedirs(destinationPath)		# if not, create one

        # Convert DatqFrame to make it compatible to csv with a "," separator
        df.to_csv(destinationPath + csvFileName, sep=',', encoding='utf-8', index=False)


