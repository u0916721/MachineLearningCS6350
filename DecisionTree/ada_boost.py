#Our ada boos algorithm
#Slightly hardcoded because we only need to do it on the bank data 
# and being generic added to much tech debt last time.
from data_cleaner import cleaner
from generic_tree import stump
from sample_weights import updateWeightsGivenMissClassifiedExamplesAndAmountOfSay

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
    testingInt = 0
    for sample in bankData.trainingData:
        testingInt += 1/amountOfSamples
        sampleWeights[tuple(sample)] = 1/amountOfSamples
    for sample in bankData.trainingData:
        sampleWeights[tuple(sample)]

    #print(f"Testing int is {testingInt} should be close to 1")
    #return (totalError,missClassfiedSamples,self.sampleWeights,self.amountOfSay)
    #updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,trainingData)
    stumpArr = []
    for i in range(0,10):
        s = stump(bankData.attributes,bankData.attributeValues,bankData.createDeepCopyTrainingData(),["yes","no"],sampleWeights)
        stumpArr.append(s)
        temp = s.calculateTotalError()
        totalError = temp[0]
        missClassfiedSamples = temp[1]
        sampleWeights = temp[2]
        amountOfSay = temp[3]
        sampleWeights = updateWeightsGivenMissClassifiedExamplesAndAmountOfSay(amountOfSay,missClassfiedSamples,sampleWeights,bankData.createDeepCopyTrainingData())
        exit()
        print(s.perdictAll(bankData.createDeepCopyTrainingData()))
    
    testingInt = 0
    for sample in bankData.trainingData:
        testingInt += sampleWeights[tuple(sample)]
    print(testingInt)
    # for sample in bankData.trainingData:
    #     sampleWeights[tuple(sample)]
    #     if tuple(sample) not in sampleWeights:
    #         exit()   
    #print(s.calculateTotalError()[0])
    return None
if __name__ == '__main__':
    runAdaBoost()
