import pandas as pd
import matplotlib.pyplot as plt

titanic_df = pd.read_csv('/home/bigdata/Downloads/train.csv')
#survived = len(titanic_df[titanic_df["Survived"] == 1])
#died = len(titanic_df[titanic_df["Survived"] == 0])

#print("Survived: ", survived)
#print("Died: ", died)

plt.plot(titanic_df["Parch"].value_counts())
plt.show() 
