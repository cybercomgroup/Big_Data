import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')

sibspFemale=[]
sibspMale=[]
sibspPer=[]
female=titanic_df[titanic_df["Sex"]=="female"]
male=titanic_df[titanic_df["Sex"]=="male"]


length=titanic_df["SibSp"].max()+1
for x in range(0,length):
	fep=len(female[female["SibSp"]==x])
	mep=len(male[male["SibSp"]==x])
	sibspFemale.append(fep)
	sibspMale.append(mep)
	if (fep+mep)>0:
		sibspPer.append(str(x)+"\n"+str(int(fep/(fep+mep)*100))+"%")
	else:
		sibspPer.append(str(x))

fig = plt.figure()
ax=fig.add_subplot(111)
bsurv=ax.bar(np.arange(length), sibspFemale,0.35,color='r')
btot=ax.bar(np.arange(length)+0.35, sibspMale,0.35,color='g')

ax.set_ylabel('Individuals')
ax.set_xlabel('SibSp\n % female')
ax.set_title('Gender distribution on SibSp')

plt.xticks(np.arange(length) + 0.35 / 2, sibspPer)

plt.show()
