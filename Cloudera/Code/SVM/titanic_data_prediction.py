import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

train_set = pd.read_csv('../Titanic_Dataset/train.csv')
test_set = pd.read_csv('../Titanic_Dataset/test.csv')

###Data preparation
train_set["Embarked"].replace("S", "0", True)
train_set["Embarked"].replace("C", "1", True)
train_set["Embarked"].replace("Q", "2", True)

train_set["Sex"].replace("male", "0", True)
train_set["Sex"].replace("female", "1", True)

del train_set["Name"]
del train_set["Cabin"]
del train_set["Ticket"]
del train_set["PassengerId"]

train_set.fillna(0, None, None, True)		
titanic_results = train_set["Survived"]
del train_set["Survived"]
###End data preparation

##Selftest
machine=svm.SVC()
machine.fit(train_set.values, titanic_results.values)
predicted_survival=machine.predict(train_set.values)

predictionSuccess=(1-np.mean(predicted_survival != titanic_results.values))*100
#print("Test against training set(self test): "+str(predictionSuccess)+"% correctness")
###End selftest


###Predict survival of test.csv
test_set["Embarked"].replace("S", "0", True)
test_set["Embarked"].replace("C", "1", True)
test_set["Embarked"].replace("Q", "2", True)

test_set["Sex"].replace("male", "0", True)
test_set["Sex"].replace("female", "1", True)

del test_set["Name"]
del test_set["Cabin"]
del test_set["Ticket"]
del test_set["PassengerId"]

test_set.fillna(0, None, None, True)	

#print(test_set.values)
test_prediction=machine.predict(test_set)
#print("Test aganst test set: "+str(test_prediction))

untouchedTest =  pd.read_csv('../Titanic_Dataset/test.csv')
untouchedTest=untouchedTest["PassengerId"]
untouchedTest['Survived']=test_prediction
untouchedTest.to_csv("predicted.csv")

###End Predict

