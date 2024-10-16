# Basic decision tree, which really is just a bunch of ID3 methods to create a tree
# Probably could put this logic in main but for now might be simpler to extract, though idk
from node import node
import random
import sample_calc

#Creates a stump that splits on the attribute
def createStump(root: node,attribute):
    # Basecase
    # len(root.attrinutes) case needed for two sample that are indentical aside from their label
    #Next tasks find the attribute with the best information gain and split on this attribute
    #Then remove the split attribute from the data set, this is an expensive call, but optimize later
    attributeSplit = attribute
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
    #root.printNode()
    return 
    # We could make these generic and pass in a math function instead that calculates each of these but
    # optimize later, make changes if needed
def createTreeInformationGainEntropy(depth,root: node,purityFunction):
    # Basecase
    # len(root.attrinutes) case needed for two sample that are indentical aside from their label
    if depth == 0 or root is None or root.hasOnlyOneLabel() or len(root.attributes) == 1:
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
        #print(trainingParition)
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
    #root.printNode()
    return 
#This is random tree learn
def createTreeInformationGainEntropyRandom(depth,root: node,purityFunction,featureSubSetSize):
    # Basecase
    # len(root.attrinutes) case needed for two sample that are indentical aside from their label
    if depth == 0 or root is None or root.hasOnlyOneLabel() or len(root.attributes) == 1:
        return
    #Next tasks find the attribute with the best information gain and split on this attribute
    if len(root.trainingDataSet) < featureSubSetSize:
        rand = random.randint(0, len(root.attributes)-1)
        attributeSplit = root.attributes[rand]
    else:
        #Next tasks find the attribute with the best information gain and split on this attribute
        subset = random.sample(root.trainingDataSet, featureSubSetSize)
        bestGain = purityFunction(root.labels,subset,root.attributes)
        #Then remove the split attribute from the data set, this is an expensive call, but optimize later
        attributeSplit = bestGain[0]
    #Then remove the split attribute from the data set, this is an expensive call, but optimize later
    #Assign it the current root as the attribute we split on
    #Assign it the current root as the attribute we split on
    root.splitAttribute = attributeSplit
    #Next we create children
    attributeValues = root.attributesValues[attributeSplit]
    #print("Splitting on " + str(attributeSplit) + " Which had a gain of " + str(bestGain[1]) + " Which has attribute values " + str(attributeValues) + " and is indexed at " +str(sample_calc.getIndexOfAttribute(attributeSplit,root.attributes)))
    # print("And has training data " + str(root.trainingDataSet))
    for a in attributeValues:
        trainingParition = sample_calc.partitionTrainingDataSetBasedOnAttributeValue(sample_calc.getIndexOfAttribute(attributeSplit,root.attributes),a,root.trainingDataSet)
        #print(trainingParition)
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
        createTreeInformationGainEntropyRandom(depth -1,c,purityFunction,featureSubSetSize)
    #root.printNode()
    return 
def printTree(tree: node):
    if not tree.children:
        print(f" split from the attributeValue {tree.splitValue} tree majority label is {tree.label}")
        print(f"its count of samples was {len(tree.trainingDataSet)}")
    else:
        print(f"splitting on {tree.splitAttribute} ")
        print(f"its count of samples was {len(tree.trainingDataSet)}")
        for c in tree.children:
            printTree(c)
def perdict(tree: node, sample):
    #Basecase
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
    if nodeToGo is None:
        return tree.label
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
    createTreeInformationGainEntropy(90000000,testNode,sample_calc.calculateBestGainME)
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
    testNode =  node(None,trainingData,attributes,attributeValues,values)
    # createStump(testNode,"T")
    # testNode.printNode()
    print

