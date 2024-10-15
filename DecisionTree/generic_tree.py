#This is a generic tree class used for assignment 2 and onwards, creates a generic tree given 
#Training Examples
#Desired depth
# attributes
#attributeVales
#and labels
#Does not do any data cleaning, expects clean data IE numerical featurs converted to categorical .

#We need the node class this is our root
from node import node
import decision_tree
import sample_calc
from data_cleaner import cleaner
from entropy_stump import calcBestAttributeToSplitOn
from entropy_stump import calcWorstAttributeToSplitOn
import math
import copy
class tree:
    #Constructor, creates a node, then creates a tree
    #Assuming that we are using GiniIndex for tree splits
    def __init__(self, trainingData,attributes,attributeValues,values,depth):
        # Set the root node of the tree
        self.rootNode = node(None,trainingData,attributes,attributeValues,values)
        # Might be usefull for debugging purposes
        self.depth = depth
        #Create the tree from the root node
        decision_tree.createTreeInformationGainEntropy(depth,self.rootNode,sample_calc.calculateBestGainGini)
class stump:
    def __init__(self,attributes,attributeValueDict,trainingData,values,sampleWeights,test=False,attr = None):
        # Set the root node of the stump
        self.rootNode = node(None,trainingData,attributes,attributeValueDict,values)
        self.trainingData = trainingData
        self.amountOfSay = 0
        self.sampleWeights = sampleWeights
        if test == False:
            attributeToSplitOn = calcBestAttributeToSplitOn(attributes,attributeValueDict,trainingData,sampleWeights)[0]
        elif attr == None:   
            attributeToSplitOn = calcWorstAttributeToSplitOn(attributes,attributeValueDict,trainingData,sampleWeights)[0]
        else:
            attributeToSplitOn = attr
        #Create the tree from the root node
        decision_tree.createStump(self.rootNode,attributeToSplitOn)
    #Return the amount of say along with the a dictionary of the misclassfied samples
    #This is so that their weights can be upweighted accordingly
    def calculateTotalError(self):
        totalError = 0
        missClassfiedSamples = set()
        for sample in self.trainingData:
            temp = self.perdict(copy.deepcopy(sample))
            perdiction = temp[0]
            #print(perdiction)
            if perdiction != sample[len(sample)-1]:
                #totalError += 1/(len(self.trainingData))
                totalError += self.sampleWeights[tuple(sample)]
                #totalError += 1
               # print(self.sampleWeights[tuple(sample)])
                missClassfiedSamples.add(tuple(sample))
        #We will set amount of say here because why not?
        #Some edge case to prevent dividing by zero
        
        if totalError == 0:
            totalError = 0.000001
        # totalError/len(self.trainingData)
        #print(totalError)
        # print(f"total error is {totalError}")
        self.amountOfSay = 0.5 * math.log((((1 - totalError) / totalError)))
        #Then we do something with this and update our weights accordingly
        #Sample weights may not be needed here but it could be usefull
        return (totalError,missClassfiedSamples,self.sampleWeights,self.amountOfSay)
    
    #Runs a perdiction given the data
    def perdictAll(self,perdictData):
        totalError = 0
        missClassfiedSamples = set()
        for sample in perdictData:
            temp = self.perdict(copy.deepcopy(sample))
            perdiction = temp[0]
            if perdiction != sample[len(sample)-1]:
                totalError += 1
        return totalError/len(perdictData)
    #Returns its perdeiction with its amount of say it was given
    def perdict(self,sample):
        return (decision_tree.perdict(self.rootNode,sample),self.amountOfSay)
   
    

# Testing portion
def test():
    attributes = ['O','T','H','W']
    values = ['yes','no']
    trainingData = []
    trainingData.append(['S','H','H','W','no'])
    trainingData.append(['S','H','H','S','no'])
    trainingData.append(['O','H','H','W','yes'])
    trainingData.append(['R','M','H','W','yes'])
    trainingData.append(['R','C','N','W','yes'])
    trainingData.append(['R','C','N','S','no'])
    trainingData.append(['O','C','N','S','yes'])
    trainingData.append(['S','M','H','W','no'])
    trainingData.append(['S','C','N','W','yes'])
    trainingData.append(['R','M','N','W','yes'])
    trainingData.append(['S','M','N','S','yes'])
    trainingData.append(['O','M','H','S','yes'])
    trainingData.append(['O','H','N','W','yes'])
    trainingData.append(['R','M','H','S','no'])
    attributeValueDict = {
                        'O': ['S', 'R', 'O'],
                        'T': ['M', 'C', 'H'],
                        'H': ['N', 'H'],
                        'W': ['S', 'W']
                         }
    d = {}
    nillWeight = len(trainingData)
    total = 0
    for t in trainingData:
        d[tuple(t)] = 1/nillWeight
    #print(calcBestAttributeToSplitOn(attributes,attributeValueDict,trainingData,d))
    s = stump(attributes,attributeValueDict,trainingData,values,d) 
if __name__ == '__main__':
    #Let write a test for a basic decision tree
    c = cleaner()
    test()
    exit()
    c.initBankData()
    c.cleanBankData(c.attributes,c.attributeValues,c.trainingData,c.testData)
    t = tree(c.createDeepCopyTrainingData(),c.attributes,c.attributeValues,c.values,100)
    #Make 100 stumps
    correct = 0
    wrong = 0
    origData = c.createDeepCopyTrainingData()
    for i in range(0,500):
        t = tree(origData,c.attributes,c.attributeValues,c.values,2)
    # for n in c.createDeepCopyTrainingData():
    #     # print(n)
    #     s = decision_tree.perdict(t.rootNode,n)
    #     if s == n[len(n)-1]:
    #         correct = correct + 1
    #     else:
    #         wrong = wrong + 1
    # noTotal = 0
    # for n in c.createDeepCopyTrainingData():
    #     if n[len(n)-1] == "no":
    #         noTotal += 1
    noder = node(None,c.createDeepCopyTrainingData(),c.attributes,c.attributeValues,c.values)
    