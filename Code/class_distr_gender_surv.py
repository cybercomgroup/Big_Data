import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to file need to be changed.
titanic_df = pd.read_csv("/home/bigdata/Downloads/train.csv")

classes = []

# We know there are First Class (1), Second (2) and Third (3)
for i in range(1,4):
    classes.append( titanic_df[ titanic_df["Pclass"] == i ] )

fem = []
male = []

# Take all females and males from every class and put in seperate lists.
for data in classes:
    fem.append( data[ data['Sex'] == 'female' ])
    male.append( data[ data['Sex'] == 'male' ])


fem_surv = []
male_surv = []


# Take all that survivec from every class and every gender and put in seperate lists.
for data in fem:
    fem_surv.append( data[ data['Survived'] == 1 ])

for data in male:
    male_surv.append( data[ data['Survived'] == 1 ])


# params(function, args[]) returns (x1, .. x-len(args)) where xi = f(args[i])
def func(f, args):
    ans = []
    for x in args:
        ans.append(f(x))
    return tuple(ans)


# Stuff to show as bar chart.
index = np.arange(3)
bar_width = 0.2
opacity = 0.7

plt.bar(index, func(len, fem), bar_width, alpha = opacity, color = 'r', label = 'Female total')
plt.bar(index + bar_width, func(len, fem_surv), bar_width, alpha = opacity, color = 'y', label = 'Female survived')
plt.bar(index + (2 * bar_width), func(len, male), bar_width, alpha = opacity, color = 'b', label = 'Male total')
plt.bar(index + (3 * bar_width), func(len, male_surv), bar_width, alpha = opacity, color = 'g', label = 'Male survived')
plt.xticks(index + bar_width + bar_width / 2, ('First class', 'Second class', 'Third class'))

plt.title("Class and Gender survival")
plt.ylabel('Count')
plt.xlabel('PClass')

plt.legend()
plt.tight_layout()
plt.show()
