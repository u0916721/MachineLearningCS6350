#Our ada boos algorithm
#Slightly hardcoded because we only need to do it on the bank data 
# and being generic added to much tech debt last time.
from data_cleaner import cleaner
from generic_tree import stump
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
        if tuple(sample) not in sampleWeights:
            exit()   
    print(f"Testing int is {testingInt} should be close to 1")
    s = stump(bankData.attributes,bankData.attributeValues,bankData.createDeepCopyTrainingData(),["yes","no"],sampleWeights)
    # for sample in bankData.trainingData:
    #     sampleWeights[tuple(sample)]
    #     if tuple(sample) not in sampleWeights:
    #         exit()   
    print(s.calculateTotalError(bankData.createDeepCopyTrainingData(),sampleWeights)[0])
    return None
if __name__ == '__main__':
    runAdaBoost()
