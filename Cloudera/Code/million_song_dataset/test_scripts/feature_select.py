import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
from sklearn.feature_selection import SelectKBest, chi2, VarianceThreshold
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification

"""
#Script for local test feature selcetion to be put on cluster
"""

#The path to train set
PATH = "train_parsed.csv"
#The feature you would like to predict
PREDICT_FEATURE = "Survived"

#Read in the file using pandas
df = pd.read_csv(PATH)

"""
Drop the feature you want to predict
"""
X = np.array(df.drop([PREDICT_FEATURE],1))
y = np.array(df[PREDICT_FEATURE])


#Drops colums which values are the same or close
"""
Do not work right now dont know why however

tmp = VarianceThreshold(threshold=(.8 *(1 - .8))).fit_transform(X)
tmp1 = VarianceThreshold(threshold=(.8 *(1 - .8))).fit_transform(y)
"""

"""
A algortim that returns a array with the least valued features droped,
Using KNN to check accuracy on how will it will predict can change that for diffrent
type of algortims uses cross_validation
"""
def feature_select_with_SelectKBest(set_X, set_Y):
    X = set_X
    y = set_Y
    resultArray =  []
    numberOfcolums = X.shape[1]
    for i in range(1,numberOfcolums):
        x_new = SelectKBest( k = i).fit_transform(X, y)
        #ger en ny array med dem bästa features na kvar, vet i fan hur jag ska spara dem
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(x_new,y,test_size = 0.2)
        clf = neighbors.KNeighborsClassifier()
        clf.fit(X_train, y_train)
        tmp = clf.score(X_test,y_test)
        resultArray.append(tmp)

    return np.argmax(resultArray)


#Feature select with SelectKBest, g
resultOfnumbers = []
testarn = []
for x in range(0,5):
    for i in range(0,500):
        koll = feature_select_with_SelectKBest(X,y)
        #print(koll)
        resultOfnumbers.append(koll)
    tmp = np.array(resultOfnumbers)
    count = np.bincount(tmp)
    testarn.append(np.argmax(count))
sistaTest = np.argmax(np.bincount(testarn))
print("Sista")
best_train_set = SelectKBest(k = sistaTest).fit_transform(X,y)
print(best_train_set)
print("programmet körs till slutet")
