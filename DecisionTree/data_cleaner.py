#This class cleans data, also prevents the overuse of readfile, which is a bottleneck
# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node
import decision_tree
import sample_calc
import copy
#Helper methods        
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
    #Does not alter the underlying data strucutre, returns a new list instead
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
def read_file(file_path,array):
    with open(file_path, mode='r') as file:
        for line in file:
            # Creates a 2d array where entry is a sample
            array.append(line.strip().split(','))
 
#This class is hardcode with the bank attributes
#The given files do not give a nice way to parese arributes,attributes values and labels
#programitcally.
#If I want to do the extrat credit I will call initExtraCreditSet
#Regardless this keeps cleaned data in one nice place           
class cleaner:
    
    def __init__(self):
        return None
    
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
        #Read in the training data
        self.trainingData = []
        self.testData = []
        relative_path = os.path.join('DataSets', 'Bank', 'debug.csv')
        read_file(relative_path,self.trainingData)
        relative_path = os.path.join('DataSets', 'Bank', 'debug.csv')
        read_file(relative_path,self.testData)
    
    #May need to make deep copies of the training data if we are required to clean the data in a diffrent way
    def createDeepCopyTrainingData(self):
        return copy.deepcopy(self.trainingData)
    def createDeepCopyTestData(self):
        return copy.deepcopy(self.testData)
    #Cleans the data, as described in the assignment requirments
    def cleanBankData(self,attributes,attributeValues,trainingData,testData):
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
if __name__ == '__main__':
    #Basic test
    c = cleaner()
    c.initBankData()
    print(c.createDeepCopyTrainingData()[0])
    c.cleanBankData(c.attributes,c.attributeValues,c.trainingData,c.testData)
    print(c.trainingData[0])