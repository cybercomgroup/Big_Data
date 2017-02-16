import pandas as pd
import numpy as np
import warnings

def setAgeGroup(sets):
	for set in sets:
		set["Age"][ np.isnan( set["Age"] ) ] = 0
		set["AgeGroup"] = set["Age"]
		set["AgeGroup"][ set["AgeGroup"] >= 65 ] = -6
		set["AgeGroup"][ set["AgeGroup"] >= 45 ] = -5
		set["AgeGroup"][ set["AgeGroup"] >= 25 ] = -4
		set["AgeGroup"][ set["AgeGroup"] >= 16 ] = -3
		set["AgeGroup"][ set["AgeGroup"] >= 5 ] = -2
		set["AgeGroup"][ set["AgeGroup"] > 0 ] = -1
		set["AgeGroup"] = set["AgeGroup"].abs().astype(int)
		set.drop("Age", axis=1, inplace=True)		
	return sets	

def setEmbarked(sets):
	for set in sets:
		set["Embarked"] = set["Embarked"].fillna("S")
		set["Embarked"][set["Embarked"] == "S"] = 0
		set["Embarked"][set["Embarked"] == "C"] = 1
		set["Embarked"][set["Embarked"] == "Q"] = 2
	return sets


def setTitleToInt(title):
	if title == "Mr":
		return 0
	elif title in ["Mrs", "Mme", "Ms"]:
		return 1
	elif title in ["Miss", "Mlle"]:
		return 2
	elif title == "Master":
		return 3
	else:
		return 4

def getTitleFromName(name):
	name = name.split(",")
	name = name[1].split(".")
	return setTitleToInt( name[0].strip() )

def parseTitle(sets):
	for set in sets:
		set["Title"] = set.apply(lambda row: getTitleFromName( row["Name"] ), axis=1 )
		set.drop("Name", axis=1, inplace=True)
	return sets

def setFamily(sets):
	for set in sets:
		set["Family"] = set["Parch"] + set["SibSp"]
		set["Family"][ set["Family"] > 0 ] = 1
		set.drop("Parch", axis=1, inplace=True)
		set.drop("SibSp", axis=1, inplace=True)
	return sets

def setGender(sets):
	for set in sets:
		set["Sex"][ set["Sex"] == "male" ] = 0
		set["Sex"][ set["Sex"] == "female" ] = 1
	return sets

warnings.filterwarnings("ignore") # This is risky, but I know the warnings are false."

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

sets = [train, test]
sets = setAgeGroup(sets)
sets = setEmbarked(sets)
sets = parseTitle(sets)
sets = setFamily(sets)
sets = setGender(sets)


for set in sets:
	set["Fare"][ np.isnan( set["Fare"] ) ] = set["Fare"].median()
	set.drop("Ticket", axis = 1, inplace = True)
	set.drop("Cabin", axis = 1, inplace = True)

sets[0].to_csv("train_parsed.csv", index = False)
sets[1].to_csv("test_parsed.csv", index = False)

print("Success.")
