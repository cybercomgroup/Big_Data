import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

titanic_df = pd.read_csv("train.csv")

titanic_df["Family"] = titanic_df["Parch"] + titanic_df["SibSp"]
titanic_df["Family"][ titanic_df["Family"] > 0] = 1

family = []

family.append( titanic_df[ titanic_df["Family"] == 1 ] )
family.append( titanic_df[ titanic_df["Family"] == 0 ] )

fam_surv = []

for data in family:
	fam_surv.append( len( data[ data["Survived"] == 1 ] ) )

family[0] = len(family[0])
family[1] = len(family[1])

index = np.arange(2)
opacity = 0.5
bar_width = 0.3

plt.bar(index, tuple(family), bar_width, alpha = opacity, color = 'g', label = "Total" )
plt.bar(index + bar_width, tuple(fam_surv), bar_width, alpha = opacity, color = 'b', label = "Survived")
plt.xticks(index + bar_width / 2, ("Family", "No Family"))
plt.legend()
plt.ylabel("Count")
plt.tight_layout()
plt.show()
