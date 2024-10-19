#This is the code for part B
#Based on your code of the decision tree learning algorithm (with infor-
#mation gain), implement a Bagged trees learning algorithm. Note that each tree
#should be fully expanded — no early stopping or post pruning. Vary the number
#of trees from 1 to 500, report how the training and test errors vary along with the
#tree number in a figure. Overall, are bagged trees better than a single tree? Are
#bagged trees better than Adaboost?
from generic_tree import tree
from data_cleaner import cleaner
from sample_with_replacement import sampleWithReplacement
from sample_with_replacement import sampleWithOutReplacement
from node import node
import decision_tree
import sample_calc
import copy

from decision_tree import perdict

def buildTree(n, sampledWithOutReplacement, bankData):
    # Bootstrapping with replacement on the sample without replacement
    bootStrappedData = sampleWithReplacement(copy.deepcopy(sampledWithOutReplacement))
    t = node(None, bootStrappedData, bankData.attributes, bankData.attributeValues, bankData.values)
    decision_tree.createTreeInformationGainEntropy(100, t, sample_calc.calculateBestGainEntropy)
    return t

def run_bagged_trees():
    # Our list of trees which grows 
    forrest = []
    bankData = cleaner()
    bankData.initBankData()
    bankData.cleanBankData(bankData.attributes,bankData.attributeValues,bankData.trainingData,bankData.testData)
    for i in range(0,500):
        bootStappedData = sampleWithReplacement(bankData.createDeepCopyTrainingData())
        # print(bankData.attributes)
        # print(bankData.attributeValues)
        # print(bankData.values)
        t = node(None,bootStappedData,bankData.attributes,bankData.attributeValues,bankData.values)
        decision_tree.createTreeInformationGainEntropy(100,t,sample_calc.calculateBestGainEntropy)
        forrest.append(t)
        right = 0
        wrong = 0
        for sample in bankData.createDeepCopyTrainingData():
            des = majorityVote(forrest, copy.deepcopy(sample))
            if des == sample[len(sample)-1]:
                right +=1
            else:
                wrong +=1
        testRight = 0
        testWrong = 0
        for sample in bankData.createDeepCopyTestData():
            des = majorityVote(forrest, copy.deepcopy(sample))
            if des == sample[len(sample)-1]:
                testRight +=1
            else:
                testWrong +=1
        print(f"{i}. Perdection error training data is {wrong/(right+wrong)} and error test data is {testWrong/(testRight+testWrong)}")
    

def runBaggedTreesSampleWithReplacement():
    forestOFForests = []
    bankData = cleaner()
    bankData.initBankData()
    bankData.cleanBankData(bankData.attributes,bankData.attributeValues,bankData.trainingData,bankData.testData)
    for i in range(0,100):
        sampledWithOutReplacemnt = sampleWithOutReplacement(bankData.createDeepCopyTrainingData(),1000)
        forest = []
        #Probably can multithread here
        for n in range(0,500):
                #I am assuming that we are then bootstrapping on the without replaced trees
                #Because we would not learn 500 of the same trees
            bootStrappedData = sampleWithReplacement(copy.deepcopy(sampledWithOutReplacemnt))
            t = node(None,bootStrappedData,bankData.attributes,bankData.attributeValues,bankData.values)
            decision_tree.createTreeInformationGainEntropy(100,t,sample_calc.calculateBestGainEntropy)
            forest.append(t)    
            print(f"Fully Expanded Tree {n} created for forest {i}") 
        forestOFForests.append(forest)
    #Now you have 100 bagged predictors in hand. For comparison, pick the first
    #tree in each run to get 100 fully expanded trees (
        print(f"Forest {i} created")
    firstTreeInEach = []
    #Finish later not very performant sadly.
    for f in forestOFForests:
        firstTreeInEach.append(f[0])
    for testExample in bankData.createDeepCopyTestData():
        majorityVote = majorityVote(firstTreeInEach,copy.deepcopy(testExample))
        
def runRandomForest():
    bankData = cleaner()
    bankData.initBankData()
    bankData.cleanBankData(bankData.attributes,bankData.attributeValues,bankData.trainingData,bankData.testData)
    for n in range(1,4):
        forrest = []
        for i in range(0,500):
            bootStappedData = sampleWithReplacement(bankData.createDeepCopyTrainingData())
        # print(bankData.attributes)
        # print(bankData.attributeValues)
        # print(bankData.values)
            t = node(None,bootStappedData,bankData.attributes,bankData.attributeValues,bankData.values)
            decision_tree.createTreeInformationGainEntropyRandom(100,t,sample_calc.calculateBestGainEntropy,n*2)
            forrest.append(t)
            right = 0
            wrong = 0
            for sample in bankData.createDeepCopyTrainingData():
                des = majorityVote(forrest, copy.deepcopy(sample))
                if des == sample[len(sample)-1]:
                    right +=1
                else:
                    wrong +=1
            testRight = 0
            testWrong = 0
            for sample in bankData.createDeepCopyTestData():
                des = majorityVote(forrest, copy.deepcopy(sample))
                if des == sample[len(sample)-1]:
                    testRight +=1
                else:
                    testWrong +=1
            print(f"{i}. Feature subset size is {n*2} Perdection error training data is {wrong/(right+wrong)} and error test data is {testWrong/(testRight+testWrong)}")
    
    return None
        
    
    
#Given some groups of classifers and a sample, output a classification
def majorityVote(forrest,sample):
    yes = 0
    no = 0
    for tree in forrest:
        perdiction = perdict(tree,copy.deepcopy(sample))
        if perdiction == "yes":
            yes+= 1
        else:
            no +=1
    if yes>= no:
        return "yes"
    else:
        return "no"
if __name__ == '__main__':
    runRandomForest()
    run_bagged_trees()