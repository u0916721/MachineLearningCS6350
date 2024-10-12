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
    #Now we put it into the hashmap
    for t in tDataArray:
        sampleWeights[tuple(t[0])] = t[1]/val
    return sampleWeights