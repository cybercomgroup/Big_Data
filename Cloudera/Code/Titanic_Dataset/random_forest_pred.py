import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train_set = pd.read_csv("train_parsed.csv")
test_set = pd.read_csv("test_parsed.csv")


target = train_set["Survived"].values
train_feat = train_set[["Pclass", "Sex", "Embarked", "AgeGroup", "Title", "Family"]].values
forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
prediction = forest.fit(train_feat, target)

print(prediction.score(train_feat, target))

test_feat = test_set[["Pclass", "Sex", "Embarked", "AgeGroup", "Title", "Family"]].values
solution = prediction.predict(test_feat)

print(prediction.feature_importances_)

PassId = np.array(test_set["PassengerId"]).astype(int)
to_print = pd.DataFrame(solution, PassId, columns = ["Survived"])

to_print.to_csv("rand_for_solution.csv", index_label = ["PassengerId"])
