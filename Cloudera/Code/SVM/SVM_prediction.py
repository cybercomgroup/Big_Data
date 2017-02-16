import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

train_set = pd.read_csv(str(sys.argv[1]))
test_set = pd.read_csv(str(sys.argv[2]))

del train_set["Fare"]
del test_set["Fare"]

choise=input("Choose kernel type(SVM):\n1)linear\n2)poly\n3)rbf\n4)sigmoid\n5)precomputed")
if choise=="1":
	choise='linear'
elif choise=="2":
	choise='poly'
elif choise=="3":
	choise='rbf'
elif choise=="4":
	choise='sigmoid'
elif choise=="5":
	choise='precomputed'
	
###Data preparation
#train_set["Embarked"].replace("S", "0", True)
#train_set["Embarked"].replace("C", "1", True)
#train_set["Embarked"].replace("Q", "2", True)

#train_set["Sex"].replace("male", "0", True)
#train_set["Sex"].replace("female", "1", True)

#del train_set["Name"]
#del train_set["Cabin"]
#del train_set["Ticket"]
del train_set["PassengerId"]

#train_set.fillna(0, None, None, True)		
titanic_results = train_set["Survived"]
del train_set["Survived"]
###End data preparation

##Selftest
machine=svm.SVC(kernel=choise)
machine.fit(train_set.values, titanic_results.values)
predicted_survival=machine.predict(train_set.values)

predictionSuccess=(1-np.mean(predicted_survival != titanic_results.values))*100
print("Test against training set(self test): "+str(predictionSuccess)+"% correctness")
###End selftest


###Predict survival of test.csv
#test_set["Embarked"].replace("S", "0", True)
#test_set["Embarked"].replace("C", "1", True)
#test_set["Embarked"].replace("Q", "2", True)

#test_set["Sex"].replace("male", "0", True)
#test_set["Sex"].replace("female", "1", True)

#del test_set["Name"]
#del test_set["Cabin"]
#del test_set["Ticket"]
del test_set["PassengerId"]

#test_set.fillna(0, None, None, True)	

#print(test_set.values)
test_prediction=machine.predict(test_set)
#print("Test aganst test set: "+str(test_prediction))

untouchedTest =  pd.read_csv('../Titanic_Dataset/test.csv')
untouchedTest=untouchedTest["PassengerId"]
untouchedTest.columns=["PassengerId"]

predictionDF=pd.DataFrame(test_prediction, np.arange(len(test_prediction)),columns=["Survived"])

joinedDF=pd.concat([untouchedTest,predictionDF], axis=1)
joinedDF.to_csv("SVM_prediction.csv",index=False)

if choise=="1":
	coeficientDF=pd.DataFrame(machine.coef_, np.arange(len(machine.coef_)),columns=["Pclass", "Sex", "Embarked", "AgeGroup", "Title", "Family"])
	coeficientDF.to_csv("linear_coeficients.csv", index=False)

###End Predict

