# This class does stuff calculating values of the sample
import math_helper
import copy

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
def calculateEntropyOfAttributeValue(ratios):
    entropy = 0.0
    for r in ratios:
        entropy = entropy + math_helper.calcEntropy(r)
    return entropy

# Takes in the ratios and calculates their Gini index
def calculateGiniIndexOfAttributeValue(ratios):
    gini = 0.0
    for r in ratios:
        gini = gini + math_helper.calcGiniIndex(r)
    return 1 - gini

# Takes in the ratios and calculates their Gini index
def calculateMEAttributeValue(ratios):
    return math_helper.calcMajorityError(ratios)


#(|Sv|/|S|) * entropy
def multiplyEntropyByTotal(total,entropy):
    return total * entropy

#(|Sv|/|S|) * entropy
def multiplyGiniByTotal(total,gini):
    return total * gini
#(|Sv|/|S|) * entropy
def multiplyMEByTotal(total,me):
    return total * me

# This is the SUM portion or |Sv|/|S| * entropy(v)
def getEntropyOfAllAttributeValues(attribute,values,labels,trainingDataSet):
    # This is |S|
    s = len(trainingDataSet)
    entropy = 0
    for v in values:
        #This is |Sv|
        sv = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributeValueCount = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributRatios = getCountOfLabelsGivenAttributeValue(attribute,v,labels,trainingDataSet,attributeValueCount)
        entropyAttributeValue = calculateEntropyOfAttributeValue(attributRatios)
        #print(str(sv) + "/" + str(s) + " * " + str(entropyAttributeValue))
        entropy = entropy + multiplyEntropyByTotal((sv/s),entropyAttributeValue)
    return entropy
# This is the SUM portion or |Sv|/|S| * entropy(v)
def getGinniOfAllAttributeValues(attribute,values,labels,trainingDataSet):
    # This is |S|
    s = len(trainingDataSet)
    gini = 0
    for v in values:
        #This is |Sv|
        sv = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributeValueCount = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributRatios = getCountOfLabelsGivenAttributeValue(attribute,v,labels,trainingDataSet,attributeValueCount)
        giniAttributeValue = calculateGiniIndexOfAttributeValue(attributRatios)
        #print(str(sv) + "/" + str(s) + " * " + str(entropyAttributeValue))
        gini = gini + multiplyGiniByTotal((sv/s),giniAttributeValue)
    return gini

# This is the SUM portion or |Sv|/|S| * entropy(v)
def getMEOfAllAttributeValues(attribute,values,labels,trainingDataSet):
    # This is |S|
    s = len(trainingDataSet)
    me = 0
    for v in values:
        #This is |Sv|
        sv = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributeValueCount = getOccurrencesOfAttributeValue(attribute,v,trainingDataSet)
        attributRatios = getCountOfLabelsGivenAttributeValue(attribute,v,labels,trainingDataSet,attributeValueCount)
        meAttributeValue = calculateMEAttributeValue(attributRatios)
        #print(str(sv) + "/" + str(s) + " * " + str(entropyAttributeValue))
        me = me + multiplyMEByTotal((sv/s),meAttributeValue)
    return me
        
def calculateBestGainEntropy(labels,trainingDataSet,attributes):
    totalEntropy = calcTotalEntropy(labels,trainingDataSet)
    #Optimization loop?
    # Rememeber attributes is a list of ints
    bestAttribute = attributes[0]
    bestValue = float('-inf')
    #Keep track of the index of the atributeValues
    indexAttribute = 0
    for a in attributes:
        gain = totalEntropy - getEntropyOfAllAttributeValues(indexAttribute,getAttributeValues(indexAttribute,trainingDataSet),labels,trainingDataSet)
        if gain > bestValue:
            bestAttribute = a
            bestValue = gain
        indexAttribute = indexAttribute + 1
    return (bestAttribute,bestValue)

def calculateBestGainGini(labels,trainingDataSet,attributes):
    totalGini = calcTotalGini(labels,trainingDataSet)
    #Optimization loop?
    # Rememeber attributes is a list of ints
    bestAttribute = attributes[0]
    bestValue = float('-inf')
    #Keep track of the index of the atributeValues
    indexAttribute = 0
    for a in attributes:
        #print("calculating gain for attribute: " + str(a))
        gain = totalGini - getGinniOfAllAttributeValues(indexAttribute,getAttributeValues(indexAttribute,trainingDataSet),labels,trainingDataSet)
        #print("Gain(S," + str(a) + ")" + " = " + str(gain))
        if gain > bestValue:
            bestAttribute = a
            bestValue = gain
        indexAttribute = indexAttribute + 1
    return (bestAttribute,bestValue)

def calculateBestGainME(labels,trainingDataSet,attributes):
    totalME = calcTotalME(labels,trainingDataSet)
    #Optimization loop?
    # Rememeber attributes is a list of ints
    bestAttribute = attributes[0]
    bestValue = float('-inf')
    #Keep track of the index of the atributeValues
    indexAttribute = 0
    for a in attributes:
        #print("calculating gain for attribute: " + str(a))
        gain = totalME - getMEOfAllAttributeValues(indexAttribute,getAttributeValues(indexAttribute,trainingDataSet),labels,trainingDataSet)
        #print("Gain(S," + str(a) + ")" + " = " + str(gain))
        if gain > bestValue:
            bestAttribute = a
            bestValue = gain
        indexAttribute = indexAttribute + 1
    return (bestAttribute,bestValue)

def calcTotalEntropy(labels,trainingDataSet):
    sizeOfWholeSet = len(trainingDataSet)
    entropy = 0
    for label in labels:
        #print(str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)) + " /" + str(sizeOfWholeSet))
        entropy = entropy + math_helper.calcEntropy(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)/sizeOfWholeSet)
    return entropy

def calcTotalGini(labels,trainingDataSet):
    sizeOfWholeSet = len(trainingDataSet)
    #print("Set size is " + str(sizeOfWholeSet))
    gini = 0
    for label in labels:
        #s = s + " + " + " "
        #print(str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)) + " /" + str(sizeOfWholeSet))
        gini = gini + math_helper.calcGiniIndex(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)/sizeOfWholeSet)
    #print("Gini index is 1 - " + s + " = " + str(1-gini))
    return 1 - gini

def calcTotalME(labels,trainingDataSet):
    sizeOfWholeSet = len(trainingDataSet)
    #print("Set size is " + str(sizeOfWholeSet))
    me = []
    for label in labels:
        #s = s + " + " + " "
        #print(str(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)) + " /" + str(sizeOfWholeSet))
        me.append(getOccurancesOfLabelGivenAttirbuteTrainingDataSet(label,trainingDataSet)/sizeOfWholeSet)
    #print("Gini index is 1 - " + s + " = " + str(1-gini))
    return 1 - max(me)

def getAttributeValues(attributeIndex,trainingDataSet):
    attributeValues = set()
    for sample in trainingDataSet:
        attributeValues.add(sample[attributeIndex])
        
    return list(attributeValues)
def getIndexOfAttribute(attribute, attributes):
    for i in range(len(attributes)):
        if attributes[i] == attribute:
            return i  
    return -1
def removeAttributeFromTrainingDataSet(attribute,trainingDataSet):
    trainingDataSetWithRemoved = copy.deepcopy(trainingDataSet)
    for sample in trainingDataSetWithRemoved:
        sample.pop(attribute)
    return trainingDataSetWithRemoved

def partitionTrainingDataSetBasedOnAttributeValue(attribute,attributeValue,trainingDataSet):
    newPartition = []
    for sample in trainingDataSet:
        if sample[attribute] == attributeValue:
            newPartition.append(sample)
    return newPartition
def removeAttributeFromAttributeList(attribute,attributes):
    newAttributes = copy.deepcopy(attributes)
    newAttributes.pop(getIndexOfAttribute(attribute,attributes))
    return newAttributes
            

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
    print("testCase12 calcTotalEntropy Pass: " + str(calcTotalEntropy(values,trainingData) == 0.9402859586706309))
    print("testCase13 getCountOfLabelsGivenAttributeValue Pass: " + str(getCountOfLabelsGivenAttributeValue(1,'C',values,trainingData,getOccurrencesOfAttributeValue(1,'C',trainingData)) == [0.75, 0.25]))
    print("testCase14 calculateEntropyOfAttributeValue Pass: " + str(getEntropyOfAllAttributeValues(0,['O','R','S'],values,trainingData) == 0.6935361388961918))
    print("testCase15 calculateBestGainEntropy Pass: " + str(calculateBestGainEntropy(values,trainingData,attributes) == ('O', 0.2467498197744391)))
    #Gini tests, example from the lecture
    giniData = []
    for i in range(5):
        giniData.append([1,"-"])
    for i in range(15):
        giniData.append([1,"+"])
    print("testCase16 calcTotalGini Pass: " + str(calcTotalGini(values,giniData) == 3/8))
    #Answer I got on the homework
    print("testCase17 calculateBestGainGini Pass: " + str(calculateBestGainGini(values,trainingData,attributes) == ('O',0.11632653061224485)))
    # Majority error tests
    print("testCase18 calcTotalMajorityError Pass: " + str(calcTotalME(values,giniData) == 1/4))
    print("testCase19 calcTotalMajorityError Pass: " + str(calcTotalME(values,trainingData) == 0.3571428571428571))
    #Calculate best gain ME
    print("testCase20 calculateBestGainME Pass: " + str(calculateBestGainME(values,trainingData,attributes) == ('O', 0.07142857142857134)))
    print("testCase21 getIndexOfAttribute Pass: " + str(getIndexOfAttribute('H',attributes) == 2))
    trainingData2 = []
    trainingData2.append(['S','H','W','-'])
    trainingData2.append(['S','H','S','-'])
    trainingData2.append(['O','H','W','+'])
    trainingData2.append(['R','M','W','+'])
    trainingData2.append(['R','C','W','+'])
    trainingData2.append(['R','C','S','-'])
    trainingData2.append(['O','C','S','+'])
    trainingData2.append(['S','M','W','-'])
    trainingData2.append(['S','C','W','+'])
    trainingData2.append(['R','M','W','+'])
    trainingData2.append(['S','M','S','+'])
    trainingData2.append(['O','M','S','+'])
    trainingData2.append(['O','H','W','+'])
    trainingData2.append(['R','M','S','-'])
    print("testCase22 testRemove Pass: " + str(trainingData2 == removeAttributeFromTrainingDataSet(getIndexOfAttribute('H',attributes),trainingData)))
    trainingData3 = []
    trainingData3.append(['R','M','H','W','+'])
    trainingData3.append(['R','C','N','W','+'])
    trainingData3.append(['R','C','N','S','-'])
    trainingData3.append(['R','M','N','W','+'])
    trainingData3.append(['R','M','H','S','-'])
    print("testCase23 testpartitionTrainingDataSetBasedOnAttributeValue Pass: " + str(trainingData3 == partitionTrainingDataSetBasedOnAttributeValue(getIndexOfAttribute('O',attributes),'R',trainingData)))
    print("testCase24 removeAttributeFromAttributeList Pass: " + str(["H","G"] == removeAttributeFromAttributeList("R",["H","G","R"])))