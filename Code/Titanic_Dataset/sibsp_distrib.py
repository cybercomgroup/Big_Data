import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')

sibspTot=[]
sibspSurv=[]
sibspPer=[]
survived=titanic_df[titanic_df["Survived"]==1]

length=titanic_df["SibSp"].max()+1
for x in range(0,length):
	tot=len(titanic_df[titanic_df["SibSp"]==x])
	surv=len(survived[survived["SibSp"]==x])
	sibspTot.append(tot)
	sibspSurv.append(surv)
	if tot!=0:
		sibspPer.append(str(x)+"\n"+str(int(surv/tot*100))+"%")
	else:
		sibspPer.append(str(x))

fig = plt.figure()
ax=fig.add_subplot(111)
bsurv=ax.bar(np.arange(length), sibspTot,0.35,color='r')
btot=ax.bar(np.arange(length)+0.35, sibspSurv,0.35,color='g')

ax.set_ylabel('Individuals')
ax.set_xlabel('SibSp\nPercent Alive')
ax.set_title('Survivors by SibSp')

plt.xticks(np.arange(length) + 0.35 / 2, sibspPer)

plt.show()
