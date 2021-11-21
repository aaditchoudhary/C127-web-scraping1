import pandas as pd
import csv
dataset1=[]
dataset2=[]
with open("main.csv",'r')as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
#print(dataset1)
with open("scrapper_2.csv",'r')as y:
    csvreader=csv.reader(y)
    for row in csvreader:
        dataset2.append(row)
#print(dataset2)
headers=dataset1[0]
#print(headers)
header2=dataset2[0]
#print(header2)
finalheaders=headers+header2
#print(finalheaders)

planetdata1=dataset1[1:]
planetdata2=dataset2[1:]
finalplanetdata=[]
#print(finalplanetdata)
for index, data_rows in enumerate(planetdata1):
    finalplanetdata.append(planetdata1[index]+planetdata2[index])
with open("finalplanets.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(finalheaders)
    csvwriter.writerows(finalplanetdata)

