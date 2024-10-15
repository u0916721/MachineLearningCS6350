#This is more so for my sanity 
#Objective of this class it return the best attribute to split on. 
#We are just going to use entropy because the assignment does not sepecfiy other wise
#This only works for the bank data set , I am not making this very generic, this is to save time
from math_helper import calcEntropy
def getTotalEntropy(dataSet,weightedSample):
    amountOfSamples = len(dataSet)
    pos = 0
    neg = 0
    for d in dataSet:
        val = d[len(d)-1]
        if val == "yes":
            pos += 1 * weightedSample[tuple(d)]
        else:
            neg += 1 * weightedSample[tuple(d)]
    # if neg + pos != amountOfSamples:
    #     #Just some error checking idk
    #     exit()
    posProb = pos / amountOfSamples
    negProb = neg / amountOfSamples
    # Calculate Gini Index
    return 1 - (posProb**2 + negProb**2)
    return posEnt + negEnt
def calculateEntOnAttributeAndAttributeValue(attribute,attributeValue,dataSet,weightedSample):
    pos = 0
    neg = 0
    total = 0
    for d in dataSet:
        val = d[attribute]
        if val == attributeValue:
            total += 1 * weightedSample[tuple(d)]
            if d[len(d)-1] == "yes":
                pos += 1 * weightedSample[tuple(d)]
                #print(weightedSample[tuple(d)])
            else:
                neg += 1 * weightedSample[tuple(d)]
                #print(weightedSample[tuple(d)])
    #Just some error checking 
    if pos == 0 or neg == 0:
        return ((0),total)
    posProb = pos/total
    #print(f"{posEnt} and pos is {pos} and total is {total}")
    negProb = neg/total
    # print(f"{posEnt} and pos is {pos} and total is {total}")
    return ((1 - (((posProb+negProb)/total)*(posProb**2 + negProb**2))),total)

def calculateEntForEntireAttribute(attribute,attributeValues,dataset,weightedSample,attributeName):
    total = len(dataset)
    ent = 0
    for aV in attributeValues:
        res = calculateEntOnAttributeAndAttributeValue(attribute,aV,dataset,weightedSample)
        numberOfExamplesWithAttributeValue = res[1]
        # entropyOfAttributeValue = res[0]
        ent += (numberOfExamplesWithAttributeValue/total) * res[0]
    return (ent,attributeName)

def calcBestAttributeToSplitOn(attributes,attributeValuesDict,dataset,weightedSample):
    bestAttribute = attributes[0]
    bestVal = float("-inf")
    totalEnt = getTotalEntropy(dataset,weightedSample)
    for i in range(0,len(attributes) - 1):
        temp = calculateEntForEntireAttribute(i,attributeValuesDict[attributes[i]],dataset,weightedSample,attributes[i])
        tempV = totalEnt - temp[0]
        tempA = temp[1]
        
        if tempV > bestVal:
            bestVal = tempV
            bestAttribute = tempA
    #print(f"splitting on {bestAttribute} with value {bestVal}")
    return (bestAttribute,bestVal)

def calcWorstAttributeToSplitOn(attributes,attributeValuesDict,dataset,weightedSample):
    bestAttribute = attributes[0]
    bestVal = float("inf")
    totalEnt = getTotalEntropy(dataset,weightedSample)
    for i in range(0,len(attributes) - 1):
        temp = calculateEntForEntireAttribute(i,attributeValuesDict[attributes[i]],dataset,weightedSample,attributes[i])
        tempV = totalEnt - temp[0]
        tempA = temp[1]
        
        if tempV < bestVal:
            bestVal = tempV
            bestAttribute = tempA
    #print(f"splitting on {bestAttribute} with value {bestVal}")
    return (bestAttribute,bestVal)


if __name__ == '__main__':
    attributes = ['O','T','H','W']
    values = ['yes','no']
    trainingData = []
    trainingData.append(['S','H','H','W','no'])
    trainingData.append(['S','H','H','S','no'])
    trainingData.append(['O','H','H','W','yes'])
    trainingData.append(['R','M','H','W','yes'])
    trainingData.append(['R','C','N','W','yes'])
    trainingData.append(['R','C','N','S','no'])
    trainingData.append(['O','C','N','S','yes'])
    trainingData.append(['S','M','H','W','no'])
    trainingData.append(['S','C','N','W','yes'])
    trainingData.append(['R','M','N','W','yes'])
    trainingData.append(['S','M','N','S','yes'])
    trainingData.append(['O','M','H','S','yes'])
    trainingData.append(['O','H','N','W','yes'])
    trainingData.append(['R','M','H','S','no'])
    attributeValueDict = {
                        'O': ['S', 'R', 'O'],
                        'T': ['M', 'C', 'H'],
                        'H': ['N', 'H'],
                        'W': ['S', 'W']
                         }
    d = {}
    nillWeight = len(trainingData)
    total = 0
    for t in trainingData:
        d[tuple(t)] = 1
    print(calcBestAttributeToSplitOn(attributes,attributeValueDict,trainingData,d))
    print(calcWorstAttributeToSplitOn(attributes,attributeValueDict,trainingData,d))
        

    
    

    
    
    
        
    
    