import csv

with open('fishData/Catch_Percent_by_Gear.csv', 'r') as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        
        print(row)