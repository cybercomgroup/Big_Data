import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')

parchTot=[]
parchSurv=[]
parchPer=[]
survived=titanic_df[titanic_df["Survived"]==1]

length=titanic_df["Parch"].max()+1
for x in range(0,length):
	tot=len(titanic_df[titanic_df["Parch"]==x])
	surv=len(survived[survived["Parch"]==x])
	parchTot.append(tot)
	parchSurv.append(surv)
	parchPer.append(str(x)+"\n"+str(int(surv/tot*100))+"%")

fig = plt.figure()
ax=fig.add_subplot(111)
bsurv=ax.bar(np.arange(length), parchTot,0.35,color='r')
btot=ax.bar(np.arange(length)+0.35, parchSurv,0.35,color='g')

ax.set_ylabel('Individuals')
ax.set_xlabel('Parch\nPercent Alive')
ax.set_title('Survivors by Parch')

plt.xticks(np.arange(length) + 0.35 / 2, parchPer)

plt.show()
