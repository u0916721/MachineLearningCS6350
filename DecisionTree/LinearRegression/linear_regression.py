#Trying something new with numpy instead of vanilla python
import numpy as np
import random

def readData(file_path):
    data = np.genfromtxt(file_path, delimiter=',')
    # Add a column of ones to the beginning of the data for the bias term
    data = np.hstack((np.ones((data.shape[0], 1)), data))  
    return data

#Calculating y_i - wTX 
#We can optimize this later
def calculateError(wT,xI):
    return xI[-1] - np.dot(wT,xI[:-1])
#See lecture 8 slide 39
def calcOneElementDeltaJ(j,weightVector,data):
    deltaJ = 0
    for s in data:
        #print(calculateYiMinusWTXI(weightVector,s))
        # print(s[j])
        deltaJ += ((calculateError(weightVector,s)) * s[j])
    return -deltaJ
#Calcuates an entire delta J
def calculateEnitireDeltaJ(weightVector,data):
    deltaJ = []
    for i in range(0,len(weightVector)):
        tempJ = calcOneElementDeltaJ(i,weightVector,data)
        deltaJ.append(tempJ)
    return np.array(deltaJ)
#Gives a new weight value
def updateWeight(weightVector,r,deltaJ):
    # print(r*deltaJ)
    # exit()
    return weightVector -( r * deltaJ)
#How we know what the best weight vector is!
#Define the cost (or loss) for a particular weight vector w to be
def costFunction(weightVector,data):
    totalCost = 0
    for d in data:
        #Square the absolute diffrence between ground truth and the perdiction
        totalCost += (d[-1] - np.dot(weightVector, d[:-1]))**2     
    return (1/2) * totalCost

def batchGradientDescent(data,r = 0.015001, b = 0,testData = None):
    #Init the base weight
    weightVector = np.zeros(data.shape[1]-1)
    while True:
        deltaJ = calculateEnitireDeltaJ(weightVector,data)
        # print("here")
        # print(deltaJ)
        newWeight = updateWeight(weightVector,r,deltaJ)
        print(f"Total error is {costFunction(newWeight,data)}")
        #print(f"Total error is {costFunction(newWeight,testData)}")
        #to examine convergence, you can watch the norm of the weight vector difference, ‖wt −wt−1‖, at eaech step t. 
        # if ‖wt −wt−1‖ is less than a tolerance level, say, 10−6, you can conclude that it converges
        #print(np.linalg.norm(newWeight - weightVector))
        if np.linalg.norm(newWeight - weightVector) <= 10**-10:
            print("Converge!")
            break
        weightVector = newWeight
    return newWeight

def stochasticGradientDescent(data,r = 0.015001, b = 0,testData = None):
    #Init the base weight
    weightVector = np.zeros(data.shape[1]-1)
    while True:
        #From lecture: Pretend the entire training set is represented by this single example
        deltaJ = calculateEnitireDeltaJ(weightVector,[data[random.randint(0, data.shape[0]-1)]])
        # print("here")
        # print(deltaJ)
        newWeight = updateWeight(weightVector,r,deltaJ)
        print(f"Total error is {costFunction(newWeight,data)}")
        print(f"Total error is {costFunction(newWeight,testData)}")
        # print(f"Total error is {costFunction(newWeight,testData)}")
        #to examine convergence, you can watch the norm of the weight vector difference, ‖wt −wt−1‖, at eaech step t. 
        # if ‖wt −wt−1‖ is less than a tolerance level, say, 10−6, you can conclude that it converges
        #print(np.linalg.norm(newWeight - weightVector))
        if np.linalg.norm(newWeight - weightVector) <= 10**-6:
            print("Converge!")
            break
        weightVector = newWeight
    return newWeight
# Eqaution taken from and explained at  https://en.wikipedia.org/wiki/Linear_regression
def analyticalForm(data):
    x = np.delete(data, -1, axis=1)
    y = data[:, -1:]
    return np.dot(np.linalg.inv(np.dot(x.T, x)), np.dot(x.T, y))

    

data = readData('train.csv')
testData = readData('test.csv')
d = analyticalForm(data)
print(d)
