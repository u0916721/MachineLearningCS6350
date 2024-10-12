#This is a class for ada boost algorithm
import math
def updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,trainingData):
    #updateAmount = sampleWeight * math.exp(amountOfSay)
    #We also need to save the amount of weights we have, hashmap does not allow duplicates.
    #How ever this means that we need to be cautios when updating the hashmap such that
    #it k -> v all sum up to one ie normalized
    #Lets do the normalization first and then do the upweighting
    tDataArray = [] # of the form ([],normalized amount)
    for sample in trainingData:
        sample = tuple(sample)
        if sample in missClassfiedSamples:
            val = sampleWeights[sample] * math.exp(amountOfSay)
            tDataArray.append((sample, val))
        else:
            val = sampleWeights[sample] * math.exp(-amountOfSay)
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

# Very simply test
def test1():
    amountOfSay = 0.5
    missClassfiedSamples = [[1, 2], [3, 4]]
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.2, (5, 6): 0.7}
    trainingData = [[1, 2], [3, 4], [5, 6]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Updated Weights are", updatedWeights)
    
# Very simply test all wrong so that all get weighted equally
def test2():
    amountOfSay = 0.9
    missClassfiedSamples = [[1, 2], [3, 4],[5,6]]
    sampleWeights = {(1, 2): 0.1, (3, 4): 0.2, (5, 6): 0.7}
    trainingData = [[1, 2], [3, 4], [5, 6]]  
    updatedWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay, missClassfiedSamples, sampleWeights, trainingData)
    print("Test2 Updated Weights are", updatedWeights)
# Very simply test all wrong so that all get weighted equally duplicate trainingData
def test3():
    amountOfSay = 0.01
    missClassfiedSamples = [[1, 2], [3, 4],[5,6]]
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
    
if __name__ == "__main__":
    #Simple test
    # test1()
    # test2()
    test3()
    test4()
    