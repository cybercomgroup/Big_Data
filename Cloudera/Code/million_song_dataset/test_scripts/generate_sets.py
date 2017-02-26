import sys
import pandas as pd
import numpy as np

def select_boundraries(previous, slength, logiclength):
    boundlength=previous
    if (logiclength)%4!=0:
        return (boundlength),((boundlength)+(slength//4+1)),(logiclength-1)
    else:
        return (boundlength),((boundlength)+slength//4),logiclength

def generate_sets(train_set, testset_index):
    splits=4
    slength = len(train_set)
    teststart,testend=[0,0]

    #Split the rows between the sets
    trainset = pd.DataFrame()
    testset = pd.DataFrame()
    logiclength=slength
    for x in range(0,splits):
        start,end,logiclength=select_boundraries(len(trainset)+len(testset), slength, logiclength)
        subset=train_set[start:end]
        if x==testset_index:
            trainset=trainset.append(subset)
        else:
            testset=testset.append(subset)

    return trainset,testset 
  




