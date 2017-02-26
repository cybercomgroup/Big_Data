import sys
import pandas as pd

def select_boundraries(previous, slength, logiclength):
    boundlength=0
    for l in previous:
        boundlength+=len(l)

    if (logiclength)%4!=0:
        return (boundlength),((boundlength)+(slength//4+1)),(logiclength-1)
    else:
        return (boundlength),((boundlength)+slength//4),logiclength

def generate_sets(train_set, testset_index):
    splits=4
    slength = len(train_set)
    
    #Split the rows between the sets
    sets = []
    logiclength=slength
    for x in range(0,splits):
        start,end,logiclength=select_boundraries(sets, slength, logiclength)
        subset=train_set[start:end]
        sets.append(subset)
    
    testset=sets.pop(testset_index)

    return sets,testset   




