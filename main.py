import pandas as pd
import json

#loading the file into this system
file = "Ford_P800_PSI5_Delta_Test_Report_Methodica.xlsx"
df = pd.read_excel(file, sheet_name= 'DTCT_Mtech')

#create new empty json file 
Jname = "output.json"
def addToJsonFile(tcNum, value):
    #creates dictionary for storing the data
    data = {}
    #for each new test case num
    if tcNum not in data:
        data[tcNum] = []
    
    #adding new vals as they are preloaded in a list
    data[tcNum].append(value)

    #save file as new add on to the dictionary
    with open(Jname, "w") as jsonFile:
        json.dump(value, jsonFile, indent = 4)

results = []
#each row will get its own data
for index, row in df.iterrows():
    tcNum = row['TC#']
    rowData = {
    "TC#": row['TC#'],
    "Test Preconditions": row['Test Preconditions'],
    "Test Procedure": row['Test Procedure'],
    "Expected Result": row['Expected Result'],
    "Actual Result": row['Actual Result']
    }
    results.append(rowData)
    addToJsonFile(tcNum, results)
