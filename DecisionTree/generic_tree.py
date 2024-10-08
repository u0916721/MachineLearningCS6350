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
    print()
    