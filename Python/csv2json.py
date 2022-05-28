import csv
import json

# CSV & Json file path
csvFile = ''
jsonFile = ''

# Open csv and read csv file
with open(csvFile, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    jsonData = []
    for csvRow in csvReader:
        jsonData.append(csvRow)

# Create json file and write json data
with open(jsonFile, 'w') as jsonFile:
    jsonFile.write(json.dumps(jsonData, indent=4, sort_keys=True))
