import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal


# I am pretty sure this entire script can be done much easier, but was basically only for learning.

titanic_df = pd.read_csv("/home/bigdata/Downloads/train.csv")

nr_females_tot = len(titanic_df[titanic_df['Sex'] == 'female'])
nr_males_tot = len(titanic_df[titanic_df['Sex'] == 'male'])

nr_females_surv = len(titanic_df[titanic_df['Sex'] == 'female'][titanic_df['Survived'] == 1])
nr_males_surv = len(titanic_df[titanic_df['Sex'] == 'male'][titanic_df['Survived'] == 1])

fem_ratio = int( round(Decimal(nr_females_surv / nr_females_tot), 2) * 100 )
male_ratio = int( round(Decimal(nr_males_surv / nr_males_tot), 2) * 100 )
fem_output = 'F Survival Rate: ' + str(fem_ratio) + '%'
male_output = 'M Survival Rate: ' + str(male_ratio) + '%'

index = np.arange(2)
bar_width = 0.35
opacity = 0.4

plt.bar(index, (nr_females_tot, nr_males_tot), bar_width, alpha = opacity, color = 'b', label = 'Total')
plt.bar(index + bar_width, (nr_females_surv, nr_males_surv), bar_width, alpha = opacity, color = 'g', label = 'Survived')

plt.ylabel('Count')
plt.xticks(index + bar_width / 2, (fem_output, male_output))
plt.legend()
plt.tight_layout()

plt.show()
