import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')

parchFemale=[]
parchMale=[]
parchPer=[]
female=titanic_df[titanic_df["Sex"]=="female"]
male=titanic_df[titanic_df["Sex"]=="male"]


length=titanic_df["Parch"].max()+1
for x in range(0,length):
	fep=len(female[female["Parch"]==x])
	mep=len(male[male["Parch"]==x])
	parchFemale.append(fep)
	parchMale.append(mep)
	parchPer.append(str(x)+"\n"+str(int(fep/(fep+mep)*100))+"%")

fig = plt.figure()
ax=fig.add_subplot(111)
bsurv=ax.bar(np.arange(length), parchFemale,0.35,color='r')
btot=ax.bar(np.arange(length)+0.35, parchMale,0.35,color='g')

ax.set_ylabel('Individuals')
ax.set_xlabel('Parch\n % female')
ax.set_title('Gender distribution on Parch')

plt.xticks(np.arange(length) + 0.35 / 2, parchPer)

plt.show()
