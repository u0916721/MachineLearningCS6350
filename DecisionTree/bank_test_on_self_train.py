# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node
import decision_tree
import sample_calc

#Our training data

# Expected that data is now a number
def mapValueGivenFeatureAndMedian(median,feature,data):
    for sample in data:
        if sample[feature] > median:
            sample[feature] = "bigger"
        else:
            sample[feature] = "lesser"

def converNumericToInt(feature,data):
    for sample in data:
        sample[feature] = int(sample[feature])
#Genric function to sort the sample given their feautre   
def sortByIndex(arr, feature):
    return sorted(arr, key=lambda x: x[feature])

def median(data,feature):
    n = len(data)
    mid = n // 2
    return data[mid][feature]

def read_file(file_path,array):
    with open(file_path, mode='r') as file:
        for line in file:
            # Creates a 2d array where entry is a sample
            array.append(line.strip().split(','))
            #Note: Do I need to extract all the possible feature values or can that be handled implicitly?
def printResults(depth,trainingData,attributes,attributeValues,values,dfunction,dfunctionName,testData):
    for i in  range(1,depth+1):
        n = node(None,trainingData,attributes,attributeValues,values)
        dfunction(i,n,sample_calc.calculateBestGainEntropy)
        totalRight = 0
        for testSample in testData:
            result = decision_tree.perdict(n,testSample)
            if result == testSample[len(testSample)-1]:
                totalRight = totalRight + 1
        print("Using " + dfunctionName + " at depth " + str(i) +" Total correct guesses is " + str(totalRight) + " out of " + str(len(testData)) + " as a percent is %" + str((totalRight/len(testData))*100))
        
def replaceUnknownAttributeWithMajority(attribute, dataSet):
    occurences = {}
    for d  in dataSet:
        if d[attribute] in occurences and d[attribute] != 'unknown':
            occurences[d[attribute]] = occurences[d[attribute]] + 1
        else:
            occurences[d[attribute]] = 1
    minVal = float('-inf')
    bestAttribute = None
    for k in  occurences:
        if occurences[k] > minVal:
            minVal = occurences[k]
            bestAttribute = k
    for d in dataSet:
        if d[attribute] == 'unknown':
            d[attribute] = bestAttribute     
    return


    
    
def runTest(depthOfTree,ID3Function,ID3FunctionName):
    #Will change with args later no need to be bogged down by those details now though.
    #Hardcode because the training data key does not give a nice way to parse this in
    attributes = [
    'age', 
    'job', 
    'marital', 
    'education', 
    'default', 
    'balance', 
    'housing', 
    'loan', 
    'contact', 
    'day', 
    'month', 
    'duration', 
    'campaign', 
    'pdays', 
    'previous', 
    'poutcome'
]
    values = ['yes', 'no'] 
    attributeValues =  {
    'age': 'numeric',
    'job': ['admin.', 'unknown', 'unemployed', 'management', 'housemaid', 'entrepreneur', 'student', 'blue-collar', 
            'self-employed', 'retired', 'technician', 'services'],
    'marital': ['married', 'divorced', 'single'],
    'education': ['unknown', 'secondary', 'primary', 'tertiary'],
    'default': ['yes', 'no'],
    'balance': 'numeric',
    'housing': ['yes', 'no'],
    'loan': ['yes', 'no'],
    'contact': ['unknown', 'telephone', 'cellular'],
    'day': 'numeric',
    'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
    'duration': 'numeric',
    'campaign': 'numeric',
    'pdays': 'numeric',
    'previous': 'numeric',
    'poutcome': ['unknown', 'other', 'failure', 'success']
    }
    trainingData = []
    testData = []
    relative_path = os.path.join('DataSets', 'Bank', 'test.csv')
    read_file(relative_path,trainingData)
    relative_path = os.path.join('DataSets', 'Bank', 'train.csv')
    read_file(relative_path,testData)
    for key in attributeValues:
        if attributeValues[key] == 'numeric':
            converNumericToInt(attributes.index(key),trainingData)
            converNumericToInt(attributes.index(key),testData)
    for key in attributeValues:
        if attributeValues[key] == 'numeric':
            trainingData = sortByIndex(trainingData,attributes.index(key))
            medianOfAttribute = median(trainingData,attributes.index(key))
            mapValueGivenFeatureAndMedian(medianOfAttribute,attributes.index(key),trainingData)
            testData = sortByIndex(testData,attributes.index(key))
            testDataMedian = median(testData,attributes.index(key))
            mapValueGivenFeatureAndMedian(testDataMedian,attributes.index(key),testData)
            attributeValues[key] = ['bigger','lesser']

    n = node(None,trainingData,attributes,attributeValues,values)
    decision_tree.createTreeInformationGainEntropy(depthOfTree,n,ID3Function)
    totalRight = 0
    for testSample in trainingData:
        result = decision_tree.perdict(n,testSample)
        if result == testSample[len(testSample)-1]:
            totalRight = totalRight + 1
    print("Using ID3 Method " + ID3FunctionName + " For depth of " + str(depthOfTree) + " Total correct guesses is " + str(totalRight) + " out of " + str(len(testData)) + " Percent is " + str((totalRight/len(testData)) * 100))
    return totalRight/len(testData)
def runTestWithUnkownReplaced(depthOfTree,ID3Function,ID3FunctionName):
    #Will change with args later no need to be bogged down by those details now though.
    #Hardcode because the training data key does not give a nice way to parse this in
    attributes = [
    'age', 
    'job', 
    'marital', 
    'education', 
    'default', 
    'balance', 
    'housing', 
    'loan', 
    'contact', 
    'day', 
    'month', 
    'duration', 
    'campaign', 
    'pdays', 
    'previous', 
    'poutcome'
]
    values = ['yes', 'no'] 
    attributeValues =  {
    'age': 'numeric',
    'job': ['admin.', 'unknown', 'unemployed', 'management', 'housemaid', 'entrepreneur', 'student', 'blue-collar', 
            'self-employed', 'retired', 'technician', 'services'],
    'marital': ['married', 'divorced', 'single'],
    'education': ['unknown', 'secondary', 'primary', 'tertiary'],
    'default': ['yes', 'no'],
    'balance': 'numeric',
    'housing': ['yes', 'no'],
    'loan': ['yes', 'no'],
    'contact': ['unknown', 'telephone', 'cellular'],
    'day': 'numeric',
    'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'],
    'duration': 'numeric',
    'campaign': 'numeric',
    'pdays': 'numeric',
    'previous': 'numeric',
    'poutcome': ['unknown', 'other', 'failure', 'success']
    }
    trainingData = []
    testData = []
    relative_path = os.path.join('DataSets', 'Bank', 'test.csv')
    read_file(relative_path,trainingData)
    relative_path = os.path.join('DataSets', 'Bank', 'train.csv')
    read_file(relative_path,testData)
    for key in attributeValues:
        if attributeValues[key] == 'numeric':
            converNumericToInt(attributes.index(key),trainingData)
            converNumericToInt(attributes.index(key),testData)
    for key in attributeValues:
        if attributeValues[key] == 'numeric':
            trainingData = sortByIndex(trainingData,attributes.index(key))
            medianOfAttribute = median(trainingData,attributes.index(key))
            mapValueGivenFeatureAndMedian(medianOfAttribute,attributes.index(key),trainingData)
            testData = sortByIndex(testData,attributes.index(key))
            testDataMedian = median(testData,attributes.index(key))
            mapValueGivenFeatureAndMedian(testDataMedian,attributes.index(key),testData)
            attributeValues[key] = ['bigger','lesser']
        replaceUnknownAttributeWithMajority(attributes.index(key),trainingData)
        replaceUnknownAttributeWithMajority(attributes.index(key),testData)
    n = node(None,trainingData,attributes,attributeValues,values)
    decision_tree.createTreeInformationGainEntropy(depthOfTree,n,ID3Function)
    totalRight = 0
    for testSample in trainingData:
        result = decision_tree.perdict(n,testSample)
        if result == testSample[len(testSample)-1]:
            totalRight = totalRight + 1
    print("Using ID3 Method " + ID3FunctionName + " For depth of " + str(depthOfTree) + " Total correct guesses is " + str(totalRight) + " out of " + str(len(trainingData)) + " Percent is " + str((totalRight/len(trainingData)) * 100))
    return totalRight/len(trainingData)
if __name__ == "__main__":
    pArray = []
    total = 0
    iDivide = 0
    for i in range(1,17):
        total = total + runTest(i,sample_calc.calculateBestGainEntropy, "Entropy")
        iDivide = iDivide + 1
    pArray.append("Entropy Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,17):
        total = total + runTest(i,sample_calc.calculateBestGainGini, "Gini")
        iDivide = iDivide + 1
    pArray.append("Gini Index Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,17):
        total = total + runTest(i,sample_calc.calculateBestGainME, "Majority Error")
        iDivide = iDivide + 1
    pArray.append("Majority Error Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    print("Now running with Unkown Replaced")
    for i in range(1,17):
        total = total + runTestWithUnkownReplaced(i,sample_calc.calculateBestGainEntropy, "Entropy")
        iDivide = iDivide + 1
    pArray.append("Entropy with Unkown Replaced Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,17):
        total = total + runTestWithUnkownReplaced(i,sample_calc.calculateBestGainGini, "Gini")
        iDivide = iDivide + 1
    pArray.append("Gini with Unkown Replaced Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,17):
        total = total + runTestWithUnkownReplaced(i,sample_calc.calculateBestGainME, "Majority Error")
        iDivide = iDivide + 1
    pArray.append("Majority Error with Unkown Replaced Percentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    
    for s in pArray:
        print(s)
    
    # printResults(20,0,0)
    #printResults(16,trainingData,attributes,attributeValues,values,decision_tree.createTreeInformationGainEntropy,"Entropy",testData)
    