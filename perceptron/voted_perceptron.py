#This is the code that contains the voted perceptron code.
#I know I could do adhere to DRY here and create generic methods, but its good practice to repeat myself in this context(learning)
#This assumes d is a numpy data frame
import numpy as np
import copy
#This is just for sanity checking on my end
from random import randint

def perceptronWeightedTrain(D,Maxiter):
    #Init weight vector to be the size of the data
    weightVector = np.zeros(len(D[0]) - 1,dtype = float) 
    weightVectors = [] # Contains a tuple array of (weightVector,score,bias)
    bias = 0
    total = 0
    for i in range(0,Maxiter):
        #Should shuffle the array on each pass optional
        #np.random.shuffle(D)
        c = 0
        for d in D:
            total += 1
            y = d[-1] # This is the true label of the sample d
            a = activationPerceptron(weightVector,d,0)
            #ya should always be positive if is correct this is the online error driven aspect of perceptron
            ya = y * a
            a = np.sign(a)
            # 0 or 1 case
            
            #Did we make an error, this is the same as y_i != y
            # as -y * -y = +y and +y * +y = y
            # if ya <= 0:
            if a != y:
                #Here make an update to the weight vector
                #Then we update the weight vector and bias
                weightVectors.append((weightVector,0,c))
                #Create a new weight vector assign its times hit value to 0
                weightVector = np.array(weightVector)
                weightVector = weightVector + y*d[:-1]
                bias = copy.deepcopy(bias) + y
                c = 0
            else:
                c +=1
    #Here we return a tuple with the weight vector and its bias 
    return (weightVectors)
#returns the activations for this sample
def activationPerceptron(weightVector,sample,bias):
    s = sample[:-1]
    return np.dot(weightVector,s) + bias
# Returns the label, given a testSample
def perceptronGuess(weightVectors,testSample):
    totalA = 0
    for w in weightVectors:
        weightVector = w[0]
        c = w[2]
        a = activationPerceptron(weightVector,testSample,w[1])
        #print(c*a)
        totalA = totalA + c * a
    #The commented code below is to see what random gguesing yields
    #To fire or not to fire
    if totalA >= 0:
        return 1
    else:
        return 0
#Given some array of vectors and their tuples compress them, such that only distinct weights remain
def compressIntoDistinctWeights(weightVectors):
    m = {}
    for w in weightVectors:
        t = (np.array2string((w[0])),w[1])
        if t in m:
            m[t] += w[2]
        else:
            m[t] = w[2]
    a = []
    for k in m:
        print(k[0])
        
        #print(np.array(eval(k[0])))
        # a.append(np.fromstring(k[0]),k[1])
    print(a)
    exit()
    return a

def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',')
    return data
def perceptronTest():
    #Read in the data in numpy 2d arrays
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    weightVectors = perceptronWeightedTrain(trainingData,10)
    totalRight = 0
    totalWrong = 0
    for td in testData:
        res = perceptronGuess(weightVectors,td)
        label = td[-1]
        #Do we fire when we are suppose to?
        passed = res == label
        if passed:
            totalRight += 1
        else:
            totalWrong += 1
    num1 = 0
    num0 = 0
    for td in testData:
        r = td[-1]
        if r == 1:
            num1+= 1
        else:
            num0 += 1
    print(f"For the test data of {len(testData)} elements the number of 1s is {num1} and the number of zeros is {num0}, ratio is {(num1/(num0+num1)) * 100} ") 
    print(f"Error rate on the test data is {(totalWrong/(totalWrong+totalRight)) * 100}")
    print(f"Total perdectied right on the test data is {(totalRight/(totalWrong+totalRight)) * 100}")
perceptronTest()