from sklearn.neighbors import NearestNeighbors
import numpy as np
X = [[0,0], [1,2], [5,3], [4,4], [2,4]]
machine=NearestNeighbors(n_neighbors=2, algorithm='ball_tree')
machine.fit(X)

guess_set =[[1,5],[0,4], [5,3]]
distances, indices = machine.kneighbors(guess_set)
print("Indices are: \n"+str(indices))
print("Distances are: \n"+str(distances))

