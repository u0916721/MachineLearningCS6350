#This is a class for ada boost algorithm
import math
import random
import copy
def updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,trainingData):
    #updateAmount = sampleWeight * math.exp(amountOfSay)
    #We also need to save the amount of weights we have, hashmap does not allow duplicates.
    #How ever this means that we need to be cautios when updating the hashmap such that
    #it k -> v all sum up to one ie normalized
    #Lets do the normalization first and then do the upweighting
    tDataArray = [] # of the form ([],normalized amount)
    for sample in trainingData:
        sample = tuple(sample)
        #print(sample)
        if sample in missClassfiedSamples:
            val = sampleWeights[sample] * math.exp(amountOfSay)
           # print(f"upweight is {val}")
            tDataArray.append((sample, val))
        else:
            val = sampleWeights[sample] * math.exp(-amountOfSay)
            #print(f"downweight is {val}")
            tDataArray.append((sample, val))
    # Next we normalize
    val = 0 
    for t in tDataArray:
        val += t[1]
    for i in range(0,len(tDataArray)):
        tDataArray[i] = (tDataArray[i][0],tDataArray[i][1]/val)
    #Now we put it into the hashmap
    for t in tDataArray:
        sampleWeights[tuple(t[0])] = t[1]
    return sampleWeights
#Assumes dataset is normalized
def generateNewRandomDistribution(sampleWeights,dataset):
    data = []
    weights = []
    for d in dataset:
        data.append(copy.deepcopy(d))
        weights.append(sampleWeights[tuple(d)])
    newArr = random.choices(data, weights = weights, k = len(dataset)-1)
    for i in range(0,len(newArr)):
        newArr[i] = copy.deepcopy(newArr[i])
    totalLength = len(dataset)
    for d in dataset:
        sampleWeights[tuple(d)] = 1/totalLength
        
        
    return copy.deepcopy(newArr)
        
        
        

# Very simply test
def test1():
    amountOfSay = 0.5
    missClassfiedSamples = {(1, 2), (3, 4)}
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.2, (5, 6): 0.7}
    trainingData = [[1, 2], [3, 4], [5, 6]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Updated Weights are", updatedWeights)
    
# Very simply test all wrong so that all get weighted equally
def test2():
    amountOfSay = 0.9
    missClassfiedSamples = {(1, 2), (3, 4)}
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.2, (5, 6): 0.7}
    trainingData = [[1, 2], [3, 4], [5, 6]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test2 Updated Weights are", updatedWeights)
# Very simply test all wrong so that all get weighted equally duplicate trainingData
def test3():
    amountOfSay = 0.01
    missClassfiedSamples = {(1, 2), (3, 4),(5,6)}
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.1, (5, 6): 0.4}
    trainingData = [[1, 2], [3, 4], [5, 6],[5,6]]  
    #Because 0.4 * 2 = 0.8 + 0.1 + 0. 1 = 1
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test3 Updated Weights are", updatedWeights)
    
# No Wrong samples perfect scenario
def test4():
    amountOfSay = 0.01
    missClassfiedSamples = []
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.1, (5, 6): 0.4}
    trainingData = [[1, 2], [3, 4], [5, 6],[5,6]]  
    #Because 0.4 * 2 = 0.8 + 0.1 + 0. 1 = 1
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test4 Updated Weights are", updatedWeights)
    
# Very simply test all wrong so that all get weighted equally
def test5():
    amountOfSay = 0.97
    missClassfiedSamples = {(1),(2),(3),(4),(5)}
    sampleWeights = {(1): 0.1, (2): 0.1, (3): 0.1, (4) : 0.1 , (5) : 0.1}
    trainingData = [[1], [2], [3],[4],[5]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test5 Updated Weights are", updatedWeights)
    
def test6():
    amountOfSay = 0.97
    missClassfiedSamples = {(8,1)}
    sampleWeights = {(1,0): 0.125, (2,0): 0.125, (3,0): 0.125, (4,0) : 0.125 , (5,0) : 0.125, (6,0) : 0.125, (7,0) : 0.125, (8,1): 0.125}
    trainingData = [[1,0], [2,0], [3,0],[4,0],[5,0],[6,0],[7,0],[8,1]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test6 Updated Weights are", updatedWeights)
    sampleWeights = updatedWeights
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test6 Updated Weights are", updatedWeights)
    
if __name__ == "__main__":
    #Simple test
    # test1()
    # test2()
    # test3()
    # test4()
    test6()
    