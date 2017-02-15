import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


titanic_df = pd.read_csv("train.csv")

titanic_df["Age"][ np.isnan( titanic_df["Age"] ) ] = 0
titanic_df["AgeGroup"] = titanic_df["Age"]

titanic_df["AgeGroup"][ titanic_df["AgeGroup"] >= 65] = -6
titanic_df["AgeGroup"][ titanic_df["AgeGroup"] >= 45] = -5
titanic_df["AgeGroup"][ titanic_df["AgeGroup"] >= 25] = -4
titanic_df["AgeGroup"][ titanic_df["AgeGroup"] >= 16] = -3
titanic_df["AgeGroup"][ titanic_df["AgeGroup"] >= 5] = -2
titanic_df["AgeGroup"][ titanic_df["AgeGroup"] > 0] = -1
titanic_df["AgeGroup"] = titanic_df["AgeGroup"].abs()

ranges = ["unknown", "0-5", "5-16", "16-25", "25-45", "45-65", "65+"]
surv = []
tot = []

for i in range(0,7):
    temp = titanic_df[ titanic_df["AgeGroup"] == i ]
    surv.append( len( temp[ temp["Survived"] == 1 ] ) )
    tot.append( len(temp) )

index = np.arange(len(ranges))
opacity = 0.5
bar_width = 0.4

plt.bar(index, tuple(tot), bar_width, alpha = opacity, color = 'g', label = 'total')
plt.bar(index + bar_width, tuple(surv), bar_width, alpha = opacity, color = 'r', label = 'survived')
plt.xticks(index + bar_width / 2, tuple(ranges))

plt.xlabel("Age")
plt.ylabel("Count")
plt.legend()
plt.show()
