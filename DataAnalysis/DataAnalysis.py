import matplotlib.pyplot as plt
import numpy as np
import csv

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

if np.mean(c2) > 160:
    print('Person needs to stay off their feet')
elif np.mean(c2) > 60 and np.mean(c2) < 160:
    print('Pressure on foot is normal')
else:
    print('Person needs to be on their feet more')