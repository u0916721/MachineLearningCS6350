#We will first implement SVM in the primal domain with stochastic sub- gradient descent. 
# We will reuse the dataset for Perceptron implementation, namely, “bank-note.zip” in Canvas.
# The features and labels are listed in the file “classification/data- desc.txt”. 
# The training data are stored in the file “classification/train.csv”, consisting of 872 examples. 
# The test data are stored in “classification/test.csv”, and comprise of 500 examples. 
# In both the training and test datasets, feature values and labels are separated by commas. 
# Set the maximum epochs T to 100. Don’t forget to shuffle the training examples at the start of each epoch. 
# Use the curve of the objective function (along with the number of updates) to diagnosis the convergence.
#Code for the primal stochastic sub gradient descent.
# We are asked to use the following for c
import numpy as np
c = [100/873,500/873,700/873]
#Might need to set a bias term here IDK
def readData(file_path):
    #Don’t forget to convert the labels to be in {1, −1}
    data = np.genfromtxt(file_path, delimiter=',')
    for d in data:
        if d[-1] == 0:
            d[-1] = -1
    return data
#Our training algorithm
def trainsgd(D,epochs,learningRate, c,a,schedule):
    np.random.seed(1)
    N = len(D)
    np.random.seed(1)
    w = np.zeros(len(D[0])-1,dtype = float)
    t = 0
    for i in range(0,epochs):
        np.random.shuffle(D)
        #t = 0
        for d in D:
            y_i = d[-1]
            x_i = d[:-1]
            if activator(y_i,w,x_i) <= 1:
                w = w - (learningRate) * w + (learningRate * c * N * y_i * x_i)
            else:
                w = (1-learningRate)*w
            t += 1
            learningRate = schedule(learningRate,t,a)
    return w

def activator(y_i,w,x_i):
    return y_i * np.dot(w,x_i)

#The learning rate schedule given for part A     
def firstSchedule(learningRate,t,a):
    return learningRate / (1 + (learningRate/a)*t)
#The learning rate schedule given for part A     
def secondSchedule(learningRate,t,a=None):
    return learningRate / (1 + t)
    
#hit current weight vector
def activate(y_i,w,x_i):
    return None


#Runs our sgd algo
def sgdTest():
    trainingData = readData('data/bank-note/train.csv')
    testData = readData('data/bank-note/test.csv')
    w = trainsgd(trainingData,100,0.1,c[0],0.1,firstSchedule)
    correct = 0
    amount = 0
    for t in testData:
        x_i = t[:-1]
        y_i = t[-1]
        res = activator(y_i,w,x_i)
        if res >= 1:
            correct += 1
        if y_i == 1:
            amount += 1
    print(f"If doing naive geussing on this data set(meaning all 1 or all -1), then our error rate is {(amount/len(testData) * 100)} or {((len(testData)-amount)/len(testData) * 100)} ")
    print(f"Total correct for the first value of C {c[0]} is {correct / len(testData) * 100}")
    return None

sgdTest()