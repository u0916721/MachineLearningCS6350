#This class cleans data, also prevents the overuse of readfile, which is a bottleneck
# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node
import decision_tree
import sample_calc

class cleaner:
    
    def __init__(self):
        print()
    
    def initBankData(self):
        self.attributes = [
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
        self.values = ['yes', 'no'] 
        self.attributeValues =  {
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