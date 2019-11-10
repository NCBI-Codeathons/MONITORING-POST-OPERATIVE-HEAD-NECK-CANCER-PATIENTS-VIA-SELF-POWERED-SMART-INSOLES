import matplotlib.pyplot as plt
import numpy as np
import csv

from twilio.rest import Client

client = Client("ACe3e83227b81823e5696955615b829feb", "180ff0ad30dc5a0ab5bcdbe00ec01b1a")

with open('analyzeData.csv','r') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    data = [i for i in r]

headings = data.pop(0)
data = np.array([[np.float(j) for j in i] for i in data])

c1 = data.T[0]
m = 0;
week1 = 0;
for m in range(0, 7, 1):
    week1 = week1 + c1[m];
    m = m + 1;
n = 7;
week2 = 0;
for n in range(7, 14, 1):
    week2 = week2 + c1[n];
    n = n + 1;
reportToDoctor = "";
if week1 < week2:
    reportToDoctor = "You have gained more weight than necessary. Contact doctor";
elif week1 > week2:
    reportToDoctor = "You have lost more weight than necessary. Contact doctor";
else:
    reportToDoctor = "You are within healthy range";  
client.messages.create(to="+1xxxxxxxxxx", 
                       from_="+1xxxxxxxxxx",
                       body=reportToDoctor)
print(reportToDoctor)