# Entry point for our application. 
import os
# Import our math helper library.
import math_helper
from node import node
import decision_tree
import sample_calc

#Our training data
trainingData = []
testData = []


def read_file(file_path,array):
    with open(file_path, mode='r') as file:
        for line in file:
            # Creates a 2d array where entry is a sample
            array.append(line.strip().split(','))
            #Note: Do I need to extract all the possible feature values or can that be handled implicitly?

if __name__ == "__main__":
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
    relative_path = os.path.join('DataSets', 'Car', 'train.csv')
    read_file(relative_path,trainingData)
    relative_path = os.path.join('DataSets', 'Car', 'test.csv')
    read_file(relative_path,testData)
    n = node(None,trainingData,attributes,attributeValues,values)
    #decision_tree.createTreeInformationGainEntropy(6,n,sample_calc.calculateBestGainEntropy)
    #decision_tree.createTreeInformationGainEntropy(6,n,sample_calc.calculateBestGainGini)
    decision_tree.createTreeInformationGainEntropy(6,n,sample_calc.calculateBestGainME)
    totalRight = 0
    for testSample in testData:
        result = decision_tree.perdict(n,testSample)
        if result == testSample[len(testSample)-1]:
            totalRight = totalRight + 1
    print("Total correct guesses is " + str(totalRight) + " out of " + str(len(testData)))
    
