import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('train.csv')

embark_splitted = []
embarked_keys = ['S', 'C', 'Q']

for ch in embarked_keys:
	embark_splitted.append( df[ df['Embarked'] == ch ] )

embark_surv = []
embark_tot = []
first_class = []
second_class = []
third_class = []

for data in embark_splitted:
	first_class.append( len( data[ data['Pclass'] == 1] ) )
	second_class.append( len( data[ data['Pclass'] == 2] ) )
	third_class.append( len( data[ data['Pclass'] == 3] ) )
	embark_surv.append( len( data[ data['Survived'] == 1 ] ) )
	embark_tot.append( len(data) )


index = np.arange(3)
opacity = 0.5
bar_width = 0.15



plt.bar(index, tuple(embark_tot), bar_width, alpha = opacity, color = 'g', label = 'Total Embarked')

plt.bar(index + bar_width, tuple(first_class), bar_width, alpha = opacity, color = 'r', label = 'First Class')
plt.bar(index + 2 * bar_width, tuple(second_class), bar_width, alpha = opacity, color = 'y', label = 'Second Class')
plt.bar(index + 3 * bar_width, tuple(third_class), bar_width, alpha = opacity, color = 'orange', label = 'Third Class')

plt.bar(index + 4 * bar_width, tuple(embark_surv), bar_width, alpha = opacity, color = 'b', label = 'Total Survived')
plt.xticks(index + 2 * bar_width , tuple(embarked_keys))
plt.legend()

plt.xlabel("Place")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
