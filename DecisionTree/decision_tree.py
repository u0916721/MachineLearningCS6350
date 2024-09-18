# Basic decision tree, which really is just a bunch of ID3 methods to create a tree
# Probably could put this logic in main but for now might be simpler to extract, though idk
from node import node
import sample_calc
    # We could make these generic and pass in a math function instead that calculates each of these but
    # optimize later, make changes if needed
def createTreeInformationGainEntropy(depth,root: node,purityFunction):
        # Basecase
    # root.printNode()
    if depth == 0 or root.hasOnlyOneLabel():
        # print()
        # print("basecase reached leaf node is below ")
        # print()
        return
        #Next tasks find the attribute with the best information gain and split on this attribute
    bestGain = purityFunction(root.labels,root.trainingDataSet,root.attributes)
    #Then remove the split attribute from the data set, this is an expensive call, but optimize later
    attributeSplit = bestGain[0]
    #Assign it the current root as the attribute we split on
    root.splitAttribute = attributeSplit
    #Next we create children
    attributeValues = root.attributesValues[attributeSplit]
    #print("Splitting on " + str(attributeSplit) + " Which had a gain of " + str(bestGain[1]) + " Which has attribute values " + str(attributeValues) + " and is indexed at " +str(sample_calc.getIndexOfAttribute(attributeSplit,root.attributes)))
    # print("And has training data " + str(root.trainingDataSet))
    for a in attributeValues:
        trainingParition = sample_calc.partitionTrainingDataSetBasedOnAttributeValue(sample_calc.getIndexOfAttribute(attributeSplit,root.attributes),a,root.trainingDataSet)
        if trainingParition:
            # Remove attribute from trainingPartition

            trainingParitionTemp = sample_calc.removeAttributeFromTrainingDataSet(sample_calc.getIndexOfAttribute(attributeSplit,root.attributes),trainingParition)
            # print()
            # print("*****")
            # print(str(trainingParitionTemp))
            # print("*****")
            # print()
            newAttributes = sample_calc.removeAttributeFromAttributeList(attributeSplit,root.attributes)
            root.children.append(node(a,trainingParitionTemp,newAttributes,root.attributesValues,root.labels))
    for c in root.children:
        # print(" Creating children for " + str(attributeSplit))
        # c.printNode()
        createTreeInformationGainEntropy(depth -1,c,purityFunction)
    return 
def perdict(tree: node, sample):
    #Basecase
    # print()
    # tree.printNode()
    # print()
    if not tree.children:
        return tree.label
    #Get the tree split attibute, this is what we are splitting on
    splitAttibute = tree.splitAttribute
    #find its indexed value in the sample
    # print(sample)
    indexedValue = sample_calc.getIndexOfAttribute(splitAttibute,tree.attributes)
    #Now get the value
    attributeValue = sample[indexedValue]
    # print(attributeValue)
    # print(splitAttibute)
    # print(indexedValue)
    # print(str(sample))
    # exit()
    nodeToGo = None
    for c in tree.children:
        if c.splitValue == attributeValue:
            nodeToGo = c
    #Given some sample ['S','H','H','W','-']
    #nodeToGo.printNode()
    sample.pop(indexedValue)
    return perdict(nodeToGo,sample)
def createTreeMajorityError():
    return None
def createTreeGiniIndex():
    return None
        
if __name__ == '__main__':
    #Main funcion of this file runs a bunch of simple tests
    #We are going to use the example given in lecture for our data
    attributes = ['O','T','H','W']
    attributeValues = {'O':['S','O','R'],'T':['H','M','C'],'H':['H','N'],'W':['W','S']}
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
    testNode =  node(None,trainingData,attributes,attributeValues,values)
    createTreeInformationGainEntropy(6,testNode,sample_calc.calculateBestGainEntropy)
    #print(str(perdict(testNode,['S','H','H','W','-'])))
    print("testCase0 perdict Pass: " + str(perdict(testNode,['S','H','H','W','-']) == '-'))
    print("testCase1 perdict Pass: " + str(perdict(testNode,['S','H','H','S','-']) == '-'))
    print("testCase2 perdict Pass: " + str(perdict(testNode,['O','H','H','W','+']) == '+'))
    print("testCase3 perdict Pass: " + str(perdict(testNode,['R','M','H','W','+']) == '+'))
    print("testCase4 perdict Pass: " + str(perdict(testNode,['R','C','N','W','+']) == '+'))
    print("testCase5 perdict Pass: " + str(perdict(testNode,['R','C','N','S','-']) == '-'))
    print("testCase6 perdict Pass: " + str(perdict(testNode,['O','C','N','S','+']) == '+'))
    print("testCase7 perdict Pass: " + str(perdict(testNode,['S','M','H','W','-']) == '-'))
    print("testCase8 perdict Pass: " + str(perdict(testNode,['S','C','N','W','+']) == '+'))
    print("testCase9 perdict Pass: " + str(perdict(testNode,['R','M','N','W','+']) == '+'))
    print("testCase10 perdict Pass: " + str(perdict(testNode,['S','M','N','S','+']) == '+'))
    print("testCase11 perdict Pass: " + str(perdict(testNode,['O','M','H','S','+']) == '+'))
    print("testCase12 perdict Pass: " + str(perdict(testNode,['O','H','N','W','+']) == '+'))
    print("testCase13 perdict Pass: " + str(perdict(testNode,['R','M','H','S','-']) == '-'))
    
    print("testCase14 perdict Pass: " + str(perdict(testNode,['S','H','H','W','+']) == '-'))
    print("testCase15 perdict Pass: " + str(perdict(testNode,['S','H','H','S','+']) == '-'))
    print("testCase16 perdict Pass: " + str(perdict(testNode,['O','H','H','W','-']) == '+'))
    print("testCase17 perdict Pass: " + str(perdict(testNode,['R','M','H','W','-']) == '+'))
    print("testCase18 perdict Pass: " + str(perdict(testNode,['R','C','N','W','-']) == '+'))
    print("testCase19 perdict Pass: " + str(perdict(testNode,['R','C','N','S','+']) == '-'))
    print("testCase20 perdict Pass: " + str(perdict(testNode,['O','C','N','S','-']) == '+'))
    print("testCase21 perdict Pass: " + str(perdict(testNode,['S','M','H','W','+']) == '-'))
    print("testCase22 perdict Pass: " + str(perdict(testNode,['S','C','N','W','-']) == '+'))
    print("testCase23 perdict Pass: " + str(perdict(testNode,['R','M','N','W','-']) == '+'))
    print("testCase24 perdict Pass: " + str(perdict(testNode,['S','M','N','S','-']) == '+'))
    print("testCase25 perdict Pass: " + str(perdict(testNode,['O','M','H','S','-']) == '+'))
    print("testCase26 perdict Pass: " + str(perdict(testNode,['O','H','N','W','-']) == '+'))
    print("testCase27 perdict Pass: " + str(perdict(testNode,['R','M','H','S','+']) == '-'))

