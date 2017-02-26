import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import generate_sets as gen
import random

whole_set = pd.read_csv(str(sys.argv[1]))

testset_index=random.randint(0,3)
train_set,test_set = gen.generate_sets(whole_set, testset_index)

train_set=train_set.fillna(0)
test_set=test_set.fillna(0)

print(len(train_set))
print(len(test_set))

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
train_results = train_set["Hottness"]
del train_set["Hottness"]
###End data preparation

##Selftest
machine=svm.SVC(kernel=choise)
machine.fit(train_set.astype(int), train_results.astype(int))
predicted_hotness=machine.predict(train_set.values)

predictionSuccess=(1-np.mean(predicted_hotness != train_results.values))*100
print("Test against training set(self test): "+str(predictionSuccess)+"% correctness")
###End selftest


###Predict survival of test.csv
#del test_set["Hottness"]
#test_prediction=machine.predict(test_set)

#predictionDF=pd.DataFrame(test_prediction, np.arange(len(test_prediction)),columns=["Survived"])
#predictionDF.to_csv("SVM_prediction.csv",index=False)

##TO BE ADAPTED BELOW
#if choise=="1":
#	coeficientDF=pd.DataFrame(machine.coef_, np.arange(len(machine.coef_)),columns=["Pclass", "Sex", "Fare", "Embarked", "AgeGroup", "Title", "Family"])
#	coeficientDF.to_csv("linear_coeficients.csv", index=False)

###End Predict
