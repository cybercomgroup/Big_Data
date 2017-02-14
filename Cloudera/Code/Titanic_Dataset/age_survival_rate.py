import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')

#Small script for learing python
#Shows age distribution and how many did not survive in a bar graph
pplDead = df[df["Survived"] == 0]
pplAge = []
pplAgeDead = []
length = df["Age"].max()

for x in range(0,int(length) + 1):
    pplAge.append(len(df[df["Age"] == x]))
    pplAgeDead.append(len(pplDead[pplDead["Age"] == x]))

tmp = [x for x in range(len(pplAge))]
tmp2 = [x for x in range(len(pplAgeDead))]
plt.ylabel("Number of people")
plt.xlabel("Age")
plt.bar(tmp, pplAge , color = "c", label = "Number of people")
plt.bar(tmp2,pplAgeDead, color = "r", label ="Number of dead people")
plt.legend()

plt.show()
