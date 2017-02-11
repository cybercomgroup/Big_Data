import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('train.csv')

class1=titanic_df[titanic_df["Pclass"]==1]
class2=titanic_df[titanic_df["Pclass"]==2]
class3=titanic_df[titanic_df["Pclass"]==3]
parchC1=[]
parchC2=[]
parchC3=[]


length=titanic_df["Parch"].max()+1
for x in range(0,length):
	parchC1.append(class1[class1["Parch"]==x])
	parchC2.append(class2[class2["Parch"]==x])
	parchC3.append(class3[class3["Parch"]==x])

fig = plt.figure()
ax=fig.add_subplot(111)
print(parchC2)

bC1=ax.bar(np.arange(length), parchC1,0.18,color='b')
bC2=ax.bar(np.arange(length)+0.18, class2,0.18,color='g')
bC3=ax.bar(np.arange(length)+0.36, class3,0.18,color='y')

ax.set_ylabel('Individuals')
ax.set_xlabel('Parch\n % female')
ax.set_title('Gender distribution on Parch')

plt.show()
