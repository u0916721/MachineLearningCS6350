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

def getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet):
    count = 0
    for sample in trainingDataSet:
        if sample[len(sample) - 1] == label:
            count = count + 1
    return count

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
def calculateEntropyOfAttributeValue(ratios,mathFunction):
    entropy = 0.0
    for r in ratios:
        entropy = entropy + mathFunction(r)
    return entropy

#(|Sv|/|S|) * entropy
def multiplyEntropyByTotal(total,entropy):
    return total * entropy

# Adds all entropy attribute values together
def sumEntropyOfAllAttributeValues(entropyList):
    return sum(entropyList)

# This is the SUM portion or |Sv|/|S| * entropy(v)
def getEntropyOfAllAttributeValues(attribute,values,labels,trainingDataSet,mathFunction):
    # This is |S|
    s = len(trainingDataSet)
    entropy = 0
    for v in values:
        #This is |Sv|
        sv = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributeValueCount = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributRatios = getCountOfLabelsGivenAttributeValue(attribute,v,labels,trainingDataSet,attributeValueCount)
        entropyAttributeValue = calculateEntropyOfAttributeValue(attributRatios,mathFunction)
        #print(str(sv) + "/" + str(s) + " * " + str(entropyAttributeValue))
        entropy = entropy + multiplyEntropyByTotal((sv/s),entropyAttributeValue)
    return entropy
        
def calculateBestGain(labels,trainingDataSet,attributes,mathFunction):
    totalEntropy = calcTotalEntropy(labels,trainingDataSet,None)
    #Optimization loop?
    # Rememeber attributes is a list of ints
    bestAttribute = attributes[0]
    bestValue = float('-inf')
    #Keep track of the index of the atributeValues
    indexAttribute = 0
    for a in attributes:
        gain = totalEntropy - getEntropyOfAllAttributeValues(indexAttribute,getAttributeValues(indexAttribute,trainingDataSet),labels,trainingDataSet,mathFunction)
        if gain > bestValue:
            bestAttribute = a
            bestValue = gain
        indexAttribute = indexAttribute + 1
    return (bestAttribute,bestValue)

def calcTotalEntropy(labels,trainingDataSet,mathFunc):
    sizeOfWholeSet = len(trainingDataSet)
    entropy = 0
    for label in labels:
        #print(str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)) + " /" + str(sizeOfWholeSet))
        entropy = entropy + math_helper.calcEntropy(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)/sizeOfWholeSet)
    return entropy

def getAttributeValues(attributeIndex,trainingDataSet):
    attributeValues = set()
    for sample in trainingDataSet:
        attributeValues.add(sample[attributeIndex])
        
    return list(attributeValues)

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
    print("testCase8 getOccurancesOfLabelGivenAttirbuteValue Pass: " + str(getOccurancesOfLabelGivenAttirbuteValue(1,'C','-',trainingData) == 1))
    print("testCase9 getOccurancesOfLabelGivenAttirbuteTrainingDataSet Pass: " + str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet('-',trainingData) == 5))
    print("testCase10 getOccurancesOfLabelGivenAttirbuteTrainingDataSet Pass: " + str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet('+',trainingData) == 9))
    print("testCase11 math_helper.calcEntropy Pass: " + str(math_helper.calcEntropy(9/14) == 0.40977637753840174))
    print("testCase12 calcTotalEntropy Pass: " + str(calcTotalEntropy(values,trainingData,None) == 0.9402859586706309))
    print("testCase13 getCountOfLabelsGivenAttributeValue Pass: " + str(getCountOfLabelsGivenAttributeValue(1,'C',values,trainingData,getOccurrencesOfAttributeValue(1,'C',trainingData)) == [0.75, 0.25]))
    print("testCase14 calculateEntropyOfAttributeValue Pass: " + str(getEntropyOfAllAttributeValues(0,['O','R','S'],values,trainingData,math_helper.calcEntropy) == 0.6935361388961918))
    print("testCase15 calculateBestGain Pass: " + str(calculateBestGain(values,trainingData,attributes,math_helper.calcEntropy) == ('O', 0.2467498197744391)))