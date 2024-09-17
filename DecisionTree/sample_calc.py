# This class does stuff calculating values of the sample
import math_helper

#Gets |S|
def getSizeofWholeSet(trainingDataSet):
    return len(trainingDataSet)

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
        entropy = entropy + multiplyEntropyByTotal((sv/s),sum(calculateEntropyOfAttributeValue(getCountOfLabelsGivenAttributeValue(attribute, v, labels, trainingDataSet,getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)))))
    return entropy
        
def calculateGain(totalEntropy, labels,trainingDataSet,attributes):
    totalEntropy = calcTotalEntropy(labels,trainingDataSet)
    #Optimization loop?
    # Rememeber attributes is a list of ints
    bestAttribute = attributes[0]
    bestValue = float('-inf')
    for a in attributes:
        gain = totalEntropy - getEntropyOfAllAttributeValues(a,getAttributeValues(a,trainingDataSet),labels,trainingDataSet)
        if gain > bestValue:
            bestAttribute = bestValue
            bestValue = gain
    return (bestAttribute,bestValue)

def calcTotalEntropy(labels,trainingDataSet):
    return

def getAttributeValues(attribute,trainingDataSet):
    return

if __name__ == '__main__':
    #Main funcion of this file runs a bunch of simple tests
    #We are going to use the example given in lecture for our data
    attributes = ['O','T','H','W']
    values = ['+','-']
    trainingData = []
    trainingData.append(['S','H','H','W','-'])
    trainingData.append(['S','H','H','S','-'])
    trainingData.append(['O','H','H','W','+'])
    trainingData.append(['R','M','H','W','+'])
    trainingData.append(['R','C','N','W','+'])
    trainingData.append(['R','C','N','S','-'])
    trainingData.append(['O','C','N','S','+'])
    trainingData.append(['S','M','H','W','-'])
    trainingData.append(['S','C','N','W','+'])
    trainingData.append(['R','M','N','W','+'])
    trainingData.append(['S','M','N','S','+'])
    trainingData.append(['O','M','H','S','+'])
    trainingData.append(['O','H','N','W','+'])
    trainingData.append(['R','M','H','S','-'])
    print("testCase0 get size of whole set Pass: " + str(getSizeofWholeSet(trainingData) == 14))
    print("testCase1 getOccurrencesOfAttributeValue Pass: " + str(getOccurrencesOfAttributeValue(0,'R',trainingData) == 5))
    print("testCase2 getOccurrencesOfAttributeValue Pass: " + str(getOccurrencesOfAttributeValue(0,'S',trainingData) == 5))
    print("testCase3 getOccurrencesOfAttributeValue Pass: " + str(getOccurrencesOfAttributeValue(0,'O',trainingData) == 4))
    print("testCase4 getOccurrencesOfAttributeValue Pass: " + str(getOccurrencesOfAttributeValue(2,'H',trainingData) == 7))
    print("testCase5 getOccurrencesOfAttributeValue Pass: " + str(getOccurrencesOfAttributeValue(2,'N',trainingData) == 7))
    print("testCase6 getOccurancesOfLabelGivenAttirbuteValue Pass: " + str(getOccurancesOfLabelGivenAttirbuteValue(1,'C','+',trainingData) == 3))
    print("testCase7 getOccurancesOfLabelGivenAttirbuteValue Pass: " + str(getOccurancesOfLabelGivenAttirbuteValue(1,'C','-',trainingData) == 1))