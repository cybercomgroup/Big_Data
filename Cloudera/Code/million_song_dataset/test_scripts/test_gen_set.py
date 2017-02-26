## This program is just to show how to utilise generate_sets.py
## to split a set into a training set and a test set.

import pandas as pd
import sys
import generate_sets as gen

test_index=0 #Choose which slice of 4 to use as test set..will be expanded to allow custom #slices
whole_set = pd.read_csv(str(sys.argv[1]))
train_set,test_set=gen.generate_sets(whole_set, 0)


#For verification
train_size=len(train_set)
print("Train set size: "+str(train_size))
print("Test set size: "+str(len(test_set)))
print("Together: "+str((train_size+len(test_set))))
print("Whole set: "+str(len(whole_set)))
