#Our ada boos algorithm
#Slightly hardcoded because we only need to do it on the bank data 
# and being generic added to much tech debt last time.
from data_cleaner import cleaner
from generic_tree import stump
from sample_weights import updateWeightsGivenMissClassifiedExamplesAndAmountOfSay
from sample_weights import generateNewRandomDistribution
from decision_tree import printTree
import copy

def printHighestWeight(sampleWeights):
    highest = float("-inf")
    r = []
    for s in sampleWeights:
        t = sampleWeights[s]
        if t > highest:
            highest = t
            r = s
    return (highest,r)
#Returns a collection of stumps that can then vote
def allPossibleStumps():
    bankData = cleaner()
    bankData.initBankData()
    bankData.cleanBankData(bankData.attributes,bankData.attributeValues,bankData.trainingData,bankData.testData)
    sampleWeights = {}
    amountOfSamples = len(bankData.trainingData)
    #Should be normalized and add to one
    numberOfYes = 0
    numberOfNo = 0
    testingInt = 0
    for sample in bankData.trainingData:
        testingInt += 1/amountOfSamples
        if sample[len(sample)-1] == "yes":
            numberOfYes += 1
        else:
            numberOfNo +=1
        sampleWeights[tuple(sample)] = 1/amountOfSamples
    for sample in bankData.trainingData:
        sampleWeights[tuple(sample)]
    for a in bankData.attributes:
                s = stump(bankData.attributes,bankData.attributeValues,bankData.createDeepCopyTrainingData(),["yes","no"],sampleWeights,True,a)
                print("Printing tree")
                printTree(s.rootNode)
                print("")
def printNice(someDict):
    for d in someDict:
        print(someDict[d])
def runAdaBoost():
    bankData = cleaner()
    bankData.initBankData()
    bankData.cleanBankData(bankData.attributes,bankData.attributeValues,bankData.trainingData,bankData.testData)
    # We want to set up our first stump
    #def __init__(self,attributes,attributeValueDict,trainingData,values,sampleWeights):
    # we need to init our sample weights
    sampleWeights = {}
    amountOfSamples = len(bankData.trainingData)
    #Should be normalized and add to one
    numberOfYes = 0
    numberOfNo = 0
    testingInt = 0
    for sample in bankData.trainingData:
        testingInt += 1/amountOfSamples
        if sample[len(sample)-1] == "yes":
            numberOfYes += 1
        else:
            numberOfNo +=1
        sampleWeights[tuple(sample)] = 1/amountOfSamples
    for sample in bankData.trainingData:
        sampleWeights[tuple(sample)]
    # print(f"The number of yes is {numberOfYes}, the number of no is {numberOfNo}")
    # exit()
    #print(f"Testing int is {testingInt} should be close to 1")
    #return (totalError,missClassfiedSamples,self.sampleWeights,self.amountOfSay)
    #updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,trainingData)
    stumpArr = []
    data = bankData.createDeepCopyTrainingData()
    b = True
    for i in range(0,500):
        s = stump(bankData.attributes,bankData.attributeValues,data,["yes","no"],sampleWeights)
        stumpArr.append(s)
        temp = s.calculateTotalError()
        totalError = temp[0]
        missClassfiedSamples = temp[1]
        sampleWeights = temp[2]
        amountOfSay = temp[3]
        # print(f"The amount of say for this stump is {amountOfSay}")
        totalRight = 0
        for samp in bankData.createDeepCopyTestData():
                tt = s.perdict(copy.deepcopy(samp))
                res = tt[0]
                say = tt[1]
                #print(say)
                if res == samp[len(samp)-1]:
                    totalRight += 1
        print(f"{i}. error on training data is {totalError}, error on test data is {(len(bankData.testData)-totalRight)/len(bankData.testData)}")           #print(1*say)
        sampleWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,copy.deepcopy(data))
        data = generateNewRandomDistribution(sampleWeights,data)
        samplesForPerdiction = bankData.createDeepCopyTestData()
        #Here we calculate our total error
        # totalRight = 0
        # totalRightTrain = 0
        # for s in samplesForPerdiction:
        #     verdict = 0
        #     for stumpy in stumpArr:
        #         tt = stumpy.perdict(copy.deepcopy(s))
        #         res = tt[0]
        #         say = tt[1]
        #         #print(say)
        #         if res == "yes":
        #             verdict += (1 * say)
        #         else:
        #             verdict += (-1*say)
        #             #print(1*say)
        #     if verdict >= 0:
        #         verdict = "yes"
        #     else:
        #         verdict = "no"
        #     actualResult = s[len(s)-1]
        #     if actualResult == verdict:
        #         totalRight += 1
        # for s in bankData.createDeepCopyTrainingData():
        #     verdict = 0
        #     for stumpy in stumpArr:
        #         tt = stumpy.perdict(copy.deepcopy(s))
        #         res = tt[0]
        #         say = tt[1]
        #         #print(say)
        #         if res == "yes":
        #             verdict += (1 * say)
        #         else:
        #             verdict += (-1*say)
        #             #print(1*say)
        #     if verdict >= 0:
        #         verdict = "yes"
        #     else:
        #         verdict = "no"
        #     actualResult = s[len(s)-1]
        #     if actualResult == verdict:
        #         totalRightTrain += 1
        
        #print(f"At itteration {i} Test data , total error of {(len(samplesForPerdiction)-totalRight)/len(samplesForPerdiction)}, Training Data, total error of {(len(samplesForPerdiction)-totalRightTrain)/len(samplesForPerdiction)}")
                    
                
                
            
        #print(s.perdictAll(bankData.createDeepCopyTrainingData()))
    
    testingInt = 0
    for sample in bankData.trainingData:
        testingInt += sampleWeights[tuple(sample)]
    #print(testingInt)
    # for sample in bankData.trainingData:
    #     sampleWeights[tuple(sample)]
    #     if tuple(sample) not in sampleWeights:
    #         exit()   
    #print(s.calculateTotalError()[0])
    return None
if __name__ == '__main__':
    runAdaBoost()
    #allPossibleStumps()
