import pandas as pd
import numpy as np
from collections import Counter
from sklearn.feature_selection import RFE
from sklearn import preprocessing, cross_validation, neighbors
import warnings
"""
Script that tells you what the worst feature to have in your train set it
only tests to remove one, will probably  make it test more in the future
Nevertheless the basic idea, is their on how feature select with cross validation
works

"""


df = pd.read_csv("train_parsed.csv")
df_test = pd.read_csv("test_parsed.csv")
df_test.drop(["PassengerId", "Fare"],1,inplace=True)
df.drop(["PassengerId", "Fare"],1, inplace=True)


features_array = ["Pclass","Sex","Embarked","AgeGroup","Title","Family"]
y = np.array(df["Survived"])


def cross_validationForFeature(N):
    if N <= 0:
        return warnings.warn("N needs to be larger then 0")
    elif N > len(features_array):
        return warnings.warn("N can not be larger then the amaount features")
    test_lastscore = []
    i = 0
    test_score = []
    if N == 1:
        for value in features_array:
            for i in range(0,20):
                x = np.array(df.drop(["Survived", value],1))
                X_train, X_test, y_train, y_test = cross_validation.train_test_split(x,y,test_size = 0.2)
                clf = neighbors.KNeighborsClassifier()
                clf.fit(X_train, y_train)
                testAccuracy = clf.score(X_test,y_test)
                test_score.append(testAccuracy)
            score_avg = np.average(test_score)
            test_lastscore.append(score_avg)
    return np.argmax(test_lastscore)
x = 0
for x in range(0,50):
    max_test = cross_validationForFeature(1)
    print("Most useless feature is: ", features_array[max_test])
