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

# Testing portion   
if __name__ == '__main__':
    #Let write a test for a basic decision tree
    c = cleaner()
    c.initBankData()
    c.cleanBankData(c.attributes,c.attributeValues,c.trainingData,c.testData)
    t = tree(c.createDeepCopyTrainingData(),c.attributes,c.attributeValues,c.values,100)
    #Make 100 stumps
    correct = 0
    wrong = 0
    for n in c.createDeepCopyTrainingData():
        # print(n)
        s = decision_tree.perdict(t.rootNode,n)
        if s == n[len(n)-1]:
            correct = correct + 1
        else:
            wrong = wrong + 1
    noTotal = 0
    for n in c.createDeepCopyTrainingData():
        if n[len(n)-1] == "no":
            noTotal += 1
    noder = node(None,c.createDeepCopyTrainingData(),c.attributes,c.attributeValues,c.values)
    