# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node
import decision_tree
import sample_calc




def read_file(file_path,array):
    with open(file_path, mode='r') as file:
        for line in file:
            # Creates a 2d array where entry is a sample
            array.append(line.strip().split(','))
            #Note: Do I need to extract all the possible feature values or can that be handled implicitly?

    
def runTest(depth, ID3Function, ID3FunctionName):
        #Will change with args later no need to be bogged down by those details now though.
    #Hardcode because the training data key does not give a nice way to parse this in
    attributes = ['buying','maint','doors','persons','lug_boot','safety']
    values = ['unacc', 'acc', 'good', 'vgood'] 
    attributeValues = {
    'buying': ['vhigh', 'high', 'med', 'low'],
    'maint': ['vhigh', 'high', 'med', 'low'],
    'doors': ['2', '3', '4', '5more'],
    'persons': ['2', '4', 'more'],
    'lug_boot': ['small', 'med', 'big'],
    'safety': ['low', 'med', 'high']
}
    trainingData = []
    testData = []
    relative_path = os.path.join('DataSets', 'Car', 'train.csv')
    read_file(relative_path,trainingData)
    relative_path = os.path.join('DataSets', 'Car', 'test.csv')
    read_file(relative_path,testData)
    n = node(None,trainingData,attributes,attributeValues,values)
    #decision_tree.createTreeInformationGainEntropy(6,n,sample_calc.calculateBestGainEntropy)
    #decision_tree.createTreeInformationGainEntropy(6,n,sample_calc.calculateBestGainGini)
    decision_tree.createTreeInformationGainEntropy(depth,n,ID3Function)
    totalRight = 0
    for testSample in trainingData:
        result = decision_tree.perdict(n,testSample)
        if result == testSample[len(testSample)-1]:
            totalRight = totalRight + 1
    print("Using ID3 Method " + ID3FunctionName + " For depth of " + str(depth) + " Total correct guesses is " + str(totalRight) + " out of " + str(len(trainingData)) + " Percent is " + str((totalRight/len(trainingData)) * 100))
    return (totalRight/(len(trainingData)))
if __name__ == "__main__":
    total = 0
    iDivide = 0
    pStr= []
    for i in range(1,7):
       total = total + runTest(i,sample_calc.calculateBestGainEntropy, "Entropy")
       iDivide = iDivide + 1
    pStr.append("Entropy Perecentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,7):
        total = total + runTest(i,sample_calc.calculateBestGainGini, "Gini")
        iDivide = iDivide + 1
    pStr.append("Gini Index Perecentage is " + str(total/iDivide))
    total = 0
    iDivide = 0
    for i in range(1,7):
        total = total + runTest(i,sample_calc.calculateBestGainME, "Majority Error")
        iDivide = iDivide + 1
    pStr.append("Majority Error Perecentage is " + str(total/iDivide))
    for p in pStr:
        print(p)
    
    
    
