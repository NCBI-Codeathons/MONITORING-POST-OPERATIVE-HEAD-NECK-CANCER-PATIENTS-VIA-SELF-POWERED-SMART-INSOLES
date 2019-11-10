import csv
import numpy
with open('testData1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    data = []
    for i in readCSV:
##        if(float(i[0]) > 0):
##            data.append((float(i[0]))
        x = float(i[0])
        if(x > 0):
            data.append(x)

weight = 2*(max(data))/3

print(weight)
print(max(data))

data2 = []

for i in data:
    if(i > weight):
        data2.append(i)


print(data2)

numpy.savetxt("analyzeData.csv", data2, delimiter=",")