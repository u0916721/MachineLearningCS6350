# This is our sample with replacement algorithm
# Takes in some data set and returns a sampled with replacement dataset.
import random
def sampleWithReplacement(dataset):
    newDataSet = []
    for i in range(0, len(dataset)):
        randNumber = random.randint(0, len(dataset)-1)
        newDataSet.append(dataset[randNumber])
    return newDataSet

def sampleWithOutReplacement(dataset,amount):
    newDataSet = []
    for i in range(0, amount):
        randNumber = random.randint(0, len(dataset)-1)
        newDataSet.append(dataset[randNumber])
        del dataset[randNumber]
    return newDataSet
    