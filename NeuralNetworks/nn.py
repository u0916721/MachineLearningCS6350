import numpy as np
import copy
# Lots of code based on the class reading http://ciml.info/dl/v0_99/ciml-v0_99-ch10.pdf
np.random.seed(1)
#https://stackoverflow.com/questions/60746851/sigmoid-function-in-numpy
def sigmoid(z):
    return 1/(1 + np.exp(-z))

#From Duame book
def networkperdict(W,v,x,hiddenUnits):
    h = np.zeros(hiddenUnits)
    for i in range(hiddenUnits):
        h[i] = np.tanh(np.dot(W[:,i], x[:-1]))
    return (np.dot(v, h))
#K is our width, this is back propagation,W with stoachisticness mixed in
#Part a and b
def networkTrain(D,leariningRate,K,MaxIter):
    np.random.seed(1)
    W = np.random.randn(D.shape[1]-1, K)
    v = np.random.randn(K)
    W = np.zeros((D.shape[1]-1, K))
    v = np.zeros(K)
    for i in range(0,MaxIter):
        #Used to check for convergence
        oldW = copy.deepcopy(W)
        G = np.zeros((D.shape[1]-1, K))
        g = np.zeros(K)
        for d in D:
            h = np.zeros(K)
            a = np.zeros(K)
            for j in range(0,K):
                a[j] = np.dot(W[:,j],d[:-1])
                h[j] =  np.tanh(a[j])
            output = np.dot(v,h)
            #output = networkperdict(W,v,d,K)
            error = d[-1] - output
            g = g - error * h
            for j in range(0,K):
                 G[:, j] -= error * v[j] * (1 - np.tanh(a[j])**2) * d[:-1]
        W = W - leariningRate * G
        v = v - leariningRate * g
        #For convergence
        if np.linalg.norm(W - oldW) <= 10**-6:  
            break
    leariningRate = updateLearningRate(leariningRate,i)  
    return [W,v]

def updateLearningRate(learningRate,i):
    return learningRate/(1 + learningRate * i)
def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',')
    return data

def toLabel(val):
    val = sigmoid(val)
    if val >= 0.5:
        return 1
    else:
        return 0
def nnTest():
    #Read in the data in numpy 2d arrays
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    widths = [5, 10, 25, 50, 100]
    for w in widths:
        result = networkTrain(trainingData,0.01,w,10000)
        W = result[0]
        v = result[1]
        right = 0
        niaveGuessing = 0
        for d in testData:
            # print(networkperdict(W,v,d,widths[4]*2))
            val = toLabel(networkperdict(W,v,d,w))
            if val == d[-1]:
                right += 1
            if  d[-1] == 0:
                niaveGuessing +=1
        print(f"Accuracy for width of test data {w} is {(right/len(testData) * 100)}")
        right = 0
        niaveGuessingTrainig = 0
        for d in trainingData:
            # print(networkperdict(W,v,d,widths[4]*2))
            val = toLabel(networkperdict(W,v,d,w))
            if val == d[-1]:
                right += 1
            if  d[-1] == 0:
                niaveGuessingTrainig +=1
        print(f"Accuracy for width training data of {w} is {(right/len(trainingData) * 100)}")
    print(f"Accuracy for naive guessing on test data is {(niaveGuessing/len(testData) * 100)}")
    print(f"Accuracy for naive guessing on training data is {(niaveGuessingTrainig/len(trainingData) * 100)}")

        
    
    
nnTest()