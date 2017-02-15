import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')
titanic_df.round({9:1})
print(titanic_df)

fareTot=[]
fareSurv=[]
farePer=[]
survived=titanic_df[titanic_df["Survived"]==1]

length=titanic_df["Fare"].max()+1

for x in np.linspace(0, length, 0.1):
	tot=len(titanic_df[titanic_df["Fare"]==x])
	surv=len(survived[survived["Fare"]==x])
	fareTot.append(tot)
	fareSurv.append(surv)
	farePer.append(str(x)+"\n"+str(int(surv/tot*100))+"%")

fig = plt.figure()
ax=fig.add_subplot(111)
bsurv=ax.bar(np.arange(length), fareTot,0.35,color='r')
btot=ax.bar(np.arange(length)+0.35, fareSurv,0.35,color='g')

ax.set_ylabel('Individuals')
ax.set_xlabel('Fare\nPercent Alive')
ax.set_title('Survivors by Fare')

plt.xticks(np.arange(length) + 0.35 / 2, farePer)

plt.show()
