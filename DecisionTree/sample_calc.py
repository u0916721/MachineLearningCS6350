# This class does stuff calculating values of the sample
import math_helper

#Gets |S|
def getSizeofWholeSet(trainingDataSet):
    return len(trainingDataSet) -1

# Gets |S_AV|
def getOccurrencesOfAttributeValue(attribute,value,trainingDataSet):
     # [[],[],[]]
     #attribute is the index of the attribute
     #and value is what we expect when we index into the array
    occurences = 0
    for sample in trainingDataSet:
        if sample[attribute] == value:
            occurences = occurences + 1
    return occurences

#Super simple at first just returns the count of all samples of attribute values that have the label
def getOccurancesOfLabelGivenAttirbuteValue(attribute,value,label,trainingDataSet):
    count = 0
    for sample in trainingDataSet:
        if sample[attribute] == value:
            if sample[len(sample)-1] == label:
                count = count + 1
    return count
# Returns the label counts given an attribute values
#Example Outlook: Sunny -> [P(2/4),N(2/4)] -> should equal one
def getCountOfLabelsGivenAttributeValue(attribute,value,labels,trainingDataSet,sizeV):
    ratios = []
    for label in labels:
        ratios.append(getOccurancesOfLabelGivenAttirbuteValue(attribute,value,label,trainingDataSet)/sizeV)  
    return ratios

# Takes in the ratios and calculates their entropy
def calculateEntropyOfAttributeValue(ratios):
    entropy = 0.0
    for r in ratios:
        entropy = entropy - math_helper.calcEntropy(r)
    return entropy

#(|Sv|/|S|) * entropy
def multiplyEntropyByTotal(total,entropy):
    return total * entropy

# Adds all entropy attribute values together
def sumEntropyOfAllAttributeValues(entropyList):
    return sum(entropyList)

# This is the SUM portion or |Sv|/|S| * entropy(v)
def getEntropyOfAllAttributeValues(attribute,values,labels,trainingDataSet):
    # This is |S|
    s = len(trainingDataSet) -1
    entropy = 0
    for v in values:
        #This is |Sv|
        sv = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        entropy = calculateEntropyOfAttributeValue(getCountOfLabelsGivenAttributeValue(attribute, v, labels, trainingDataSet,getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)))

        
    