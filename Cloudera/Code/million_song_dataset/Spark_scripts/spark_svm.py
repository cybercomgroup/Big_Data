#from pyspark import SparkConf
#from pyspark import SparkContext
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import random
from sklearn.preprocessing import Imputer
from sklearn import tree


def rddToPand(RDD):

	header = "temp"
	first = True
	data = []

	# Convert unicode to ascii
	for x in RDD.collect():
		if first:
			first = False
			header = x.encode("ascii").split(',')

		else:
			data.append(tuple(x.encode("ascii").split(',')))

	return pd.DataFrame.from_records(data, columns = header)

####Run the local job
####Train SVM+feature selection+cross validation
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
train_set = pd.read_csv(str(sys.argv[1]))
#train_set.fillna(0)

#print(train_set["Song_Hottness"])

#Data preparation
target = train_set["Song_Hottness"].values

train_set = train_set.drop("Song_Hottness", axis = 1)
train_set = train_set.fillna(0)
features = train_set.values

#End data preparation

#train_header=list(train_set.columns.values)



#Set NaN values to mean for the column
#train_results=train_results.reshape(-1,1)
#imp.fit(train_results)
#temp2=imp.transform(train_results)
#train_results=pd.DataFrame(temp2, np.arange(len(temp2)), columns=['Song_Hottness'])
#imp.fit(train_set)
#temp=imp.transform(train_set)
#train_set=pd.DataFrame(temp, np.arange(len(temp)), columns=train_header)

#print("Length set: "+str(len(train_set)))
#print("Length train: "+str(len(train_results)))

print("Any NANS: "+str(np.any(np.isnan(train_set))))
print("Any Finite: "+str(np.any(np.isfinite(train_set))))

choise=input("Choose kernel type(SVM):\n1)linear\n2)poly\n3)rbf\n4)sigmoid\n5)precomputed\n\n > ")
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

#Selftest
#print(list(train_results.values.ravel()))
machine = svm.SVC(gamma = 0.001, kernel = 'linear')

machine = machine.fit(features, target.astype(int))

#machine.fit(X, Y) #list(temp2.ravel()) <- Gives -some- effect..but doesn't work


predicted_hotness=machine.predict(train_set.values)

predictionSuccess=(1-np.mean(predicted_hotness != train_results.values))*100
print("Test against training set(self test): "+str(predictionSuccess)+"% correctness")
#End selftest

####Run the distributed job
####Prediction on test set
# Init Spark
#conf = SparkConf()
#conf.setMaster('yarn-client')
#conf.setAppName('mapreduce-job')
#sc = SparkContext(conf=conf)

#rdd = sc.textFile(str(sys.argv[2]))
#whole_set=rddToPand(rdd)


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
