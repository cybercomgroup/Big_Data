import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import matplotlib.pyplot as plt

"""
Small script to test k Nearest neighbors on the titanic set
got a 72 procent correctly on kaggle
Using sklearn package algortims
Supervised machine learning
"""

df = pd.read_csv("train_parsed.csv")
df_test = pd.read_csv("test_parsed.csv")

df_test.drop(["PassengerId", "Fare"],1,inplace=True)
df.drop(["PassengerId", "Fare"],1, inplace=True)

X = np.array(df.drop(["Survived"],1))
Y = np.array(df["Survived"])
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,Y,test_size = 0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)

testAccuracy = clf.score(X_test,Y_test)
print(testAccuracy)
measures = np.array(df_test)
measures = measures.reshape(len(measures), -1)
print(len(measures))
predict = clf.predict(measures)
print(predict)

tmp1 = []
tmp2 = []
i = 892 # because PassengerId starts at 892
for data in predict:
    tmp1.append([i,data])
    i += 1

csv_file = np.array(tmp1)
np.savetxt("result.csv",csv_file, delimiter=',', header='PassengerId,Survived',fmt="%i", comments='')
