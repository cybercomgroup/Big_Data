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

for data in embark_splitted:
	embark_surv.append( len( data[ data['Survived'] == 1 ] ) )
	embark_tot.append( len(data) )


index = np.arange(3)
opacity = 0.5
bar_width = 0.4

plt.bar(index, tuple(embark_tot), bar_width, alpha = opacity, color = 'b', label = 'Total Embarked')
plt.bar(index + bar_width, tuple(embark_surv), bar_width, alpha = opacity, color = 'r', label = 'Total Survived')
plt.xticks(index + bar_width / 2, tuple(embarked_keys))
plt.legend()

plt.xlabel("Place")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
