import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Seperate titles, French -> english, others to rare.
def engTitle(title):
	if title in ["Miss", "Mrs", "Mr", "Dr", "Master"]:
		return title
	elif title in ["Mme", "Ms"]:
		return "Mrs"
	elif title == "Mlle":
		return "Miss"
	else:
		return "Rare" #Include Major, Sir, the Countess, Lady, Jonkheer, Rev etc

def getTitleFromName(name):
	name = name.split(",")
	name = name[1].split(".")
	return engTitle( name[0].strip() )

df = pd.read_csv("train.csv")
df["Title"] = df.apply(lambda row: getTitleFromName(row["Name"]), axis = 1)

titles = df["Title"].unique()
index = np.arange( len(titles) )
opacity = 0.5
bar_width = 0.3

total = []
survived = []

for title in titles:
	t_all = df[ df["Title"] == title ]
	total.append( len(t_all) )
	survived.append( len( t_all[ t_all["Survived"] == 1] ) )

for i in range(0, len(titles)):
	s = titles[i] + "\t-\t tot: " + str(total[i]) + ", surv: " + str(survived[i]) + ", ratio: " + str(survived[i] / total[i])
	print(s)

plt.bar(index, tuple(total), bar_width, alpha = opacity, color = 'b', label = "Total" )
plt.bar(index + bar_width, tuple(survived), bar_width, alpha = opacity, color = 'r', label = "Survived" )
plt.xlabel("Title")
plt.ylabel("Count")

plt.legend()
plt.xticks(index + bar_width / 2, tuple(titles) )
plt.show()

