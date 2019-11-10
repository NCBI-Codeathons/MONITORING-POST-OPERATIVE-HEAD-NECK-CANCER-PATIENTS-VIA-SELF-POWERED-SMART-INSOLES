import matplotlib.pyplot as plt
import numpy as np
import csv

from twilio.rest import Client

client = Client("ACe3e83227b81823e5696955615b829feb", "180ff0ad30dc5a0ab5bcdbe00ec01b1a")

with open('test_d1.csv','r') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    data = [i for i in r]

headings = data.pop(0)
data = np.array([[np.float(j) for j in i] for i in data])

c1 = data.T[0]
c2 = data.T[1]

fig, ax = plt.subplots(1)
ax.plot(c1, c2)
plt.xlabel('Time')
plt.ylabel('Pressure')
fig.show()
personWeight = 150;
rangePercentage = 0.2
m = 0;
reportToDoctor = "You are within healthy range";
while m < len(c2):
    if (c2[m] < ((rangePercentage * personWeight) - personWeight)):
        reportToDoctor = "You have lost more weight than necessary. Contact doctor";
    elif (c2[m] > ((rangePercentage * personWeight) + personWeight)):
        reportToDoctor = "You have gained more weight than necessary. Contact doctor";
    else:
        m = m + 1;
#client.messages.create(to="+15127390615", 
#                       from_="+12055399840",
#                       body=reportToDoctor)
print(reportToDoctor)