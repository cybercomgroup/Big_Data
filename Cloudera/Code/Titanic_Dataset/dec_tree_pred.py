import numpy as np
import pandas as pd
from sklearn import tree

train_set = pd.read_csv("train_parsed.csv")
test_set = pd.read_csv("test_parsed.csv")

train_target = train_set["Survived"].values
train_feat = train_set[["Pclass", "Sex", "Embarked", "AgeGroup", "Title", "Family"]].values

tree_model = tree.DecisionTreeClassifier()
tree_model = tree_model.fit(train_feat, train_target)

print(tree_model.feature_importances_)
print(tree_model.score(train_feat, train_target))

test_feat = test_set[["Pclass", "Sex", "Embarked", "AgeGroup", "Title", "Family"]].values
pred = tree_model.predict(test_feat)

PassId = np.array(test_set["PassengerId"]).astype(int)
solution = pd.DataFrame(pred, PassId, columns = ["Survived"])

print(solution.shape)
solution.to_csv("dec_tree_solution.csv", index_label = ["PassengerId"])
